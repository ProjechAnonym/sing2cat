import OUT_JSON as outbound
import DNS_JSON as dns
import ROUTE_JSON as route
import CLASH_JSON as clash
import json
def configGenerate(path,internal_dns,external_dns,proxy_search_dns,ttl,external_tag,hyjack,ips,ports,domains,uiport,uiurl,uikey):
    return {
        "log": {
        "disabled": bool(None),
        "level": "info",
        "output": "/var/singbox/box.log",
        "timestamp": bool("true")
        },
        "dns":dns.dnsOut(internal_dns,external_dns,proxy_search_dns,ttl,external_tag),
        "inbounds": [{"type": "tun",
                      "tag": "tun-in",
                      "inet4_address": "172.19.0.1/30",
                      "mtu": 1500,
                      "auto_route": bool("true"),
                      "strict_route": bool(None),
                      "stack": "gvisor",
                      "sniff": bool("true"),
                      "sniff_override_destination": bool(None)}],
        "outbounds":outbound.generateOutbound(path,hyjack,ips,ports,domains),
        "route":route.routeJson(external_tag,hyjack,domains),
        "experimental": clash.generateClash(uiport,uiurl,external_tag,uikey)
        }
# config_json = json.dumps(configGenerate("代理配置\奈云机场配置.yml",
#                                         "https://223.5.5.5/dns-query",
#                                         "https://8.8.8.8/dns-query",
#                                         "https://1.1.1.1/dns-query",
#                                         10800,
#                                         'select',
#                                         True,["192.168.234.3"],[9090],["clash.com"],
#                                         ),ensure_ascii=False)
# with open(r"代理配置/config.json","w",encoding="utf-8") as config:
#     config.write(config_json)

def GenerateJsonFile(yaml_path,write_path,dns_list,ttl=10800,external_tag='select',hyjack=False,ips=None,ports=None,domains=None,uiport=9090,uiurl="https://github.com/MetaCubeX/Yacd-meta/archive/gh-pages.zip",uikey="123456"):
    config_json = json.dumps(configGenerate(yaml_path,
                                        dns_list[0],
                                        dns_list[1],
                                        dns_list[2],
                                        ttl,
                                        external_tag,
                                        hyjack,ips,ports,domains,
                                        uiport,uiurl,uikey
                                        ),ensure_ascii=False)
    with open(f"{write_path}/config.json","w",encoding="utf-8") as config:
        config.write(config_json)
    return True