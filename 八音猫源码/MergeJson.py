import DnsModule as dns
import ExperimentalModule as exp
import OutModule as outbound
import RouteModule as route
import TemplateProcess as tp
import ProcessHyjack as ph
import json
def MergeJson(yaml_path,dns_list,ttl,hyjack,ips,ports,domains,uiport,uiurl,uikey):
    if hyjack:
        route_json = route.RouteJson(hyjack,ph.Outbounds(ips,ports),ips,ports,domains)
    else:
        route_json = route.RouteJson(hyjack,None,None,None,None)
    return {"log":tp.log,'dns':dns.DNSjson(dns_list,ttl),"inbounds":tp.inbound,
            "outbounds":outbound.MergeOutJson(yaml_path,hyjack,ips,ports),
            "route":route_json,
            "experimental":exp.ClashDash(uiport,uiurl,uikey)}
def SaveJsonFile(yaml_path,write_path,dns_list,ttl=10800,hyjack=False,ips=None,ports=None,domains=None,uiport=9090,uiurl="https://github.com/MetaCubeX/Yacd-meta/archive/gh-pages.zip",uikey="123456"):
    config_json = json.dumps(MergeJson(yaml_path,dns_list,ttl,
                                        hyjack,ips,ports,domains,
                                        uiport,uiurl,uikey
                                        ),ensure_ascii=False)
    with open(f"{write_path}/config.json","w",encoding="utf-8") as config:
        config.write(config_json)
    return True
