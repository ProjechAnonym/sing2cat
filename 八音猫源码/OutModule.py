import yaml
import TemplateProcess as tp
import ProcessHyjack
import re
def loadNodes(yaml_path):
    with open(f"{yaml_path}",encoding="utf-8") as f:
        yaml_file = yaml.load(f,yaml.BaseLoader)
        nodes = yaml_file['proxies']
    return nodes
def Yaml2Json(nodes):
    node_tag = [None]*len(nodes)
    node_json = [None]*len(nodes)
    for node in range(len(nodes)):
        node_tag[node] = nodes[node]["name"]
        if nodes[node]["type"] == "ss":
            node_json[node] = tp.ssJson(nodes[node]).copy()
        elif nodes[node]["type"] == "vmess":
            node_json[node] = tp.vmessJson(nodes[node]).copy()
        else:
            node_json[node] = tp.trojanJson(nodes[node]).copy()
    return node_json,node_tag
def HyjackHost(ip,port,tags):
    return {"type":"direct","tag":tags,"override_address":ip,"override_port":port}
def autoOut(out_tags):
    return {
            "type": "urltest",
            "tag": "auto",
            "outbounds": out_tags,
            "url": "https://www.gstatic.com/generate_204",
            "interval": "5m",
            "tolerance": 100,
            "interrupt_exist_connections": False
           }
def selectOut(out_tags):
    select_list = out_tags.copy()
    select_list.append("auto")
    return {"type": "selector",
            "tag": "select",
            "outbounds":select_list,
            "default": "auto",
            "interrupt_exist_connections": False
           }
def MergeOutJson(yaml_path,hyjack,ips,ports):
    nodes_yaml = loadNodes(yaml_path)
    [nodes_json,nodes_tag] = Yaml2Json(nodes_yaml)
    auto_out = autoOut(nodes_tag)
    select_out = selectOut(nodes_tag)
    if hyjack:
        host_outboud = ProcessHyjack.Outbounds(ips,ports)
        lan_tag = [None]*len(host_outboud.keys())
        default_out = [None]*(5+len(nodes_tag)+len(lan_tag))
        index = 0
        for des in host_outboud.keys():
            ips_ports = re.split(':',des)
            lan_tag[index] = HyjackHost(ips_ports[0],int(ips_ports[1]),f"lan{host_outboud[des]}")
            default_out[index] = lan_tag[index]
            index = index + 1
        for proxy in range(len(nodes_json)):
            default_out[len(lan_tag)+proxy] = nodes_json[proxy]
        default_out[len(lan_tag)+len(nodes_tag)] = select_out
        default_out[len(lan_tag)+len(nodes_tag)+1] = auto_out
        default_out[len(lan_tag)+len(nodes_tag)+2] = {"type":"direct","tag":"direct"}
        default_out[len(lan_tag)+len(nodes_tag)+3] = {"type":"dns","tag":"dns-out"}
        default_out[len(lan_tag)+len(nodes_tag)+4] = {"type":"block","tag":"block"}
    else:
        default_out = [None]*(5+len(nodes_tag))
        for proxy in range(len(nodes_json)):
            default_out[proxy] = nodes_json[proxy]
        default_out[len(nodes_tag)] = select_out
        default_out[len(nodes_tag)+1] = auto_out
        default_out[len(nodes_tag)+2] = {"type":"direct","tag":"direct"}
        default_out[len(nodes_tag)+3] = {"type":"dns","tag":"dns-out"}
        default_out[len(nodes_tag)+4] = {"type":"block","tag":"block"}
    return default_out


