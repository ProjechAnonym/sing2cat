import json
def loadTemplate():
    with open(r'.\config\template.json','r',encoding="utf-8") as f:
        template = json.load(f)
    return template
template = loadTemplate()
inbound = template["inbound"]
log = template["log"]
ss = template["ss"]
vmess = template["vmess"]
trojan = template["trojan"]
geoip_db = template["geoip"]
geosite_db = template["geosite"]
dns = template['dns']
quic = template['quic']
foreign_rule = template['foreign']
cn_rule = template['cn']
site_private = template['site_private']
ip_private = template['ip_private']
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
    return vmess
def trojanJson(node):
    trojan["tag"] = node["name"]
    trojan["server"] = node["server"]
    trojan["server_port"] = int(node["port"])
    trojan["password"] = node["password"]
    trojan["tls"]["server_name"] = node["sni"]
    return trojan
