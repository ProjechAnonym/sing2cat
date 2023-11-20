import TemplateProcess as tp
def RouteRules(hyjack,outbound_dict,ips,ports,domains):
    default_rules = []
    if hyjack:
        hyjack_rules = [None]*len(domains)
        for domain in range(len(domains)):
            num = outbound_dict[f"{ips[domain]}:{ports[domain]}"]
            hyjack_rules[domain] = {"domain":domains[domain],"outbound":f"lan{num}"}
            default_rules.append(hyjack_rules[domain])
        default_rules.append(tp.dns)
        default_rules.append(tp.quic)
        default_rules.append(tp.foreign_rule)
        default_rules.append(tp.cn_rule)
        default_rules.append(tp.site_private)
        default_rules.append(tp.ip_private)
    else:
        default_rules.append(tp.dns)
        default_rules.append(tp.quic)
        default_rules.append(tp.foreign_rule)
        default_rules.append(tp.cn_rule)
        default_rules.append(tp.site_private)
        default_rules.append(tp.ip_private)
    return default_rules
def RouteJson(hyjack,outbound_dict,ips,ports,domains):
    return {"geoip":tp.geoip_db,
            "geosite":tp.geosite_db,
            "rules": RouteRules(hyjack,outbound_dict,ips,ports,domains),
            "auto_detect_interface": True
            }
