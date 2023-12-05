from . import DnsModule as dns
from . import ExperimentalModule as exp
from . import OutModule as outbound
from . import RouteModule as route
from . import TemplateProcess as tp
from . import ProcessHyjack as ph
import json
def MergeJson(dns_list,ttl,hyjack,ips,ports,domains,uiport,uiurl,uikey):
    if hyjack:
        route_json = route.RouteJson(hyjack,ph.Outbounds(ips,ports),ips,ports,domains)
    else:
        route_json = route.RouteJson(hyjack,None,None,None,None)
    return {"log":tp.log,'dns':dns.DNSjson(dns_list,ttl),"inbounds":tp.inbound,
            "outbounds":outbound.MergeOutJson(hyjack,ips,ports),
            "route":route_json,
            "experimental":exp.ClashDash(uiport,uiurl,uikey)}
def SaveJsonFile(write_path,dns_list,ttl=10800,hyjack=False,ips=None,ports=None,domains=None,uiport=9090,uiurl="ui",uikey="123456"):
    config_json = json.dumps(MergeJson(dns_list,ttl,
                                        hyjack,ips,ports,domains,
                                        uiport,uiurl,uikey
                                        ),ensure_ascii=False)
    with open(f"{write_path}/config.json","w",encoding="utf-8") as config:
        config.write(config_json)
    return True
