from . import TemplateProcess as tp
def RouteRules(hyjack,outbound_dict,ips,ports,domains):
    default_rules = []
    if hyjack:
        hyjack_rules = [None]*len(domains)
        for domain in range(len(domains)):
            num = outbound_dict[f"{ips[domain]}:{ports[domain]}"]
            hyjack_rules[domain] = {"domain":domains[domain],"outbound":f"lan{num}"}
            default_rules.append(hyjack_rules[domain])
        default_rules.append(tp.dns)
        default_rules.append(tp.private_ip)
        default_rules.append(tp.quic)
        default_rules.append(tp.foreign_rule)
        default_rules.append(tp.cn_rule)
    else:
        default_rules.append(tp.dns)
        default_rules.append(tp.private_ip)
        default_rules.append(tp.quic)
        default_rules.append(tp.foreign_rule)
        default_rules.append(tp.cn_rule)
    return default_rules
def RouteJson(hyjack,outbound_dict,ips,ports,domains):
    return {"rule_set":tp.rule_set,
            "rules": RouteRules(hyjack,outbound_dict,ips,ports,domains),
            "final":tp.final,
            "auto_detect_interface": True
            }
