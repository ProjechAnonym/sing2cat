import yaml,requests,copy
from . import protocolPart
from config import GlobalVars
def getNodes():
    urls = GlobalVars.getValues("url")
    for index,url in enumerate(urls):
        try:
            with requests.get(url,timeout=30) as res:
                content = res.content.decode("utf-8")
            if index == 0:
                nodes = yaml.load(content,Loader=yaml.BaseLoader)["proxies"]
            else:
                nodes.extend(yaml.load(content,Loader=yaml.BaseLoader)["proxies"])
        except Exception as e:
            print(f"获取机场链接出错,{e}")
    if nodes:
        return nodes
    else:
        return False
def formatnodes():
    nodes = getNodes()
    tags = [None]*len(nodes)
    nodes_json = [None]*len(nodes)
    for index,node in enumerate(nodes):
        if node['type'] == 'vmess':
            node_json = protocolPart.vmess(node)
            nodes_json[index] = copy.deepcopy(node_json)
            tags[index] = node_json['tag']
        elif node['type'] == 'ss':
            node_json = protocolPart.shadowsocks(node)
            nodes_json[index] = copy.deepcopy(node_json)
            tags[index] = node_json['tag']
        elif node['type'] == 'trojan':
            node_json = protocolPart.trojan(node)
            nodes_json[index] = copy.deepcopy(node_json)
            tags[index] = node_json['tag']
    return [tags,nodes_json]
def selectOut(tags):
    select_node = GlobalVars.getValues('outbounds')['select']
    select_node['outbounds'] = copy.deepcopy(tags)
    select_node['outbounds'].append('auto')
    return select_node
def autoOut(tags):
    auto_node = GlobalVars.getValues("outbounds")['auto']
    auto_node['outbounds'] = tags
    return auto_node
def outboundsConfig():
    tag,nodes = formatnodes()
    rule_sets = GlobalVars.getValues('rule_set')
    nodes.append(copy.deepcopy(selectOut(tag)))
    if rule_sets:
        for key in rule_sets.keys():
            if not rule_sets[key]['china']:
                rule_set_select_node = selectOut(tag)
                rule_set_select_node['tag'] = f"{key}-select"
                nodes.append(copy.deepcopy(rule_set_select_node))
    nodes.append(autoOut(tag))
    nodes.append(GlobalVars.getValues("outbounds")['direct'])
    nodes.append(GlobalVars.getValues("outbounds")['dns_out'])
    nodes.append(GlobalVars.getValues("outbounds")['block'])
    return nodes

