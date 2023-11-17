import yaml
def getProxy(path):
    with open(f"{path}",encoding="utf-8") as f:
        yaml_file = yaml.load(f,yaml.BaseLoader)
        proxies = yaml_file['proxies']
    return proxies

def getProxyJson(proxies):
    ss = {"type":"shadowsocks",
        "tag":"",
        "server":"",
        "server_port":"",
        "method":"",
        "password":""
        }
    vmess = {"type":"vmess",
            "tag":"",
            "server":"",
            "server_port":"",
            "uuid":"",
            "security":"auto",
            "transport":{"type": "ws",
                        "path": "/",
                        "early_data_header_name": "Sec-WebSocket-Protocol"
                        }
            }
    trojan = {"type":"trojan",
            "tag":"",
            "server":"",
            "server_port":"",
            "password": "",
            "tls": {
                "enabled": bool("true"),
                "disable_sni": bool(None),
                "server_name": "",
                "insecure": bool("true")
                    }
            }
    proxies_json = [0]*len(proxies)
    proxies_tag = [0]*len(proxies)
    for i in range(len(proxies)):
        proxies_tag[i] = proxies[i]["name"]
        if proxies[i]["type"] == "ss":
            ss["tag"] = proxies[i]["name"]
            ss["server"] = proxies[i]["server"]
            ss["server_port"] = int(proxies[i]["port"])
            ss["method"] = proxies[i]["cipher"]
            ss["password"] = proxies[i]["password"]
            proxies_json[i] = ss.copy()
        elif proxies[i]["type"] == "vmess":
            vmess["tag"] = proxies[i]["name"]
            vmess["server"] = proxies[i]["server"]
            vmess["server_port"] = int(proxies[i]["port"])
            vmess["uuid"] = proxies[i]["uuid"]
            proxies_json[i] = vmess.copy()
        else:
            trojan["tag"] = proxies[i]["name"]
            trojan["server"] = proxies[i]["server"]
            trojan["server_port"] = int(proxies[i]["port"])
            trojan["password"] = proxies[i]["password"]
            trojan["tls"]["server_name"] = proxies[i]["sni"]
            proxies_json[i] = trojan.copy()
    return proxies_json,proxies_tag

def hyjackHost(dip,dport,tag):
    return {"type":"direct","tag":tag,"override_address":dip,"override_port":dport}

def autoOut(proxy_tag):
    return {
            "type": "urltest",
            "tag": "auto",
            "outbounds": proxy_tag,
            "url": "https://www.gstatic.com/generate_204",
            "interval": "5m",
            "tolerance": 100,
            "interrupt_exist_connections": bool(None)
           }
def selectOut(proxy_tag):
    temp = proxy_tag.copy()
    temp.append("auto")
    return {"type": "selector",
            "tag": "select",
            "outbounds":temp,
            "default": "auto",
            "interrupt_exist_connections": bool(None)
           }   

def generateOutbound(path,hyjack,ips,ports,tags):
    proxy_yaml = getProxy(path)
    [proxy_json,proxy_tag] = getProxyJson(proxy_yaml)
    default_json = [{"type":"direct","tag":"direct"},{"type":"dns","tag":"dns-out"},{"type":"block","tag":"block"}]
    if hyjack:
        lan_tag = [0]*len(ips)
        for i in range(len(ips)):
            lan_tag[i] = hyjackHost(ips[i],ports[i],tags[i])
            default_json.append(lan_tag[i])
        auto_out = autoOut(proxy_tag)
        select_out = selectOut(proxy_tag)
        for j in range(len(proxy_json)):
            default_json.append(proxy_json[j])
        default_json.append(auto_out)
        default_json.append(select_out)
        return default_json
    else:
        auto_out = autoOut(proxy_tag)
        select_out = selectOut(proxy_tag)
        for j in range(len(proxy_json)):
            default_json.append(proxy_json[j])
        default_json.append(auto_out)
        default_json.append(select_out)
        return default_json


