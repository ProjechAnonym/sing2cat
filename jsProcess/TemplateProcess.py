import json
def loadTemplate():
    with open(r'.\static\config\template.json','r',encoding="utf-8") as f:
        template = json.load(f)
    return template
template = loadTemplate()
inbound = template["inbound"]
log = template["log"]
ss = template["ss"]
vmess = template["vmess"]
trojan = template["trojan"]
rule_set = template["rule_set"]
dns = template['dns']
quic = template['quic']
private_ip = template["private"]
foreign_rule = template['foreign']
cn_rule = template['cn']
final = template["final"]
cache = template["cache_file"]
def ssJson(node):
    ss["tag"] = node["name"]
    ss["server"] = node["server"]
    ss["server_port"] = int(node["port"])
    ss["method"] = node["cipher"]
    ss["password"] = node["password"]
    return ss
def vmessJson(node):
    vmess["tag"] = node["name"]
    vmess["server"] = node["server"]
    vmess["server_port"] = int(node["port"])
    vmess["uuid"] = node["uuid"]
    if "ws-path" in node.keys():
        vmess["transport"]["path"] = node["ws-path"]
    if "ws-headers" in node.keys():
        vmess["transport"]["headers"] = node["ws-headers"]
    return vmess
def trojanJson(node):
    trojan["tag"] = node["name"]
    trojan["server"] = node["server"]
    trojan["server_port"] = int(node["port"])
    trojan["password"] = node["password"]
    trojan["tls"]["server_name"] = node["sni"]
    return trojan
