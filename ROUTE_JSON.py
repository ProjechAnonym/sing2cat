def generateRules(hyjack,domains,external_tag):
    default_rule = [{"protocol": "dns","outbound": "dns-out"},{"protocol": ["quic"],"outbound": "block"}]
    if hyjack:
        hyjack_rules = [None]*len(domains)
        for i in range(len(domains)):
            hyjack_rules[i] = {"domain":domains[i],"outbound":domains[i]}
            default_rule.append(hyjack_rules[i])
        default_rule.append({"type": "logical",
                             "mode": "and",
                             "rules": [{"geosite": ["geolocation-!cn"]},
                                       {"geoip": ["cn"],
                                        "invert": bool("true")}],
                                        "outbound": f"{external_tag}"})
        default_rule.append({"type": "logical",
                             "mode": "and",
                             "rules": [{"geosite": ["cn"]},
                                       {"geoip": ["cn"]}],
                                       "outbound": "direct"})
        default_rule.append({"geosite": ["private"],
                             "outbound": "direct"})
        default_rule.append({"geoip": ["cn", "private"],
                             "outbound": "direct"})
    else:
        default_rule.append({"type": "logical",
                             "mode": "and",
                             "rules": [{"geosite": ["geolocation-!cn"]},
                                       {"geoip": ["cn"],
                                        "invert": bool("true")}],
                                        "outbound": f"{external_tag}"})
        default_rule.append({"type": "logical",
                             "mode": "and",
                             "rules": [{"geosite": ["cn"]},
                                       {"geoip": ["cn"]}],
                                       "outbound": "direct"})
        default_rule.append({"geosite": ["private"],
                             "outbound": "direct"})
        default_rule.append({"geoip": ["cn", "private"],
                             "outbound": "direct"})
    return default_rule
def routeJson(external_tag,hyjack=False,domains=None):
    return {"geoip": {"download_url": "https://github.com/soffchen/sing-geoip/releases/latest/download/geoip.db",
                      "download_detour": f"{external_tag}"},
            "geosite": {"download_url": "https://github.com/soffchen/sing-geosite/releases/latest/download/geosite.db",
                      "download_detour": f"{external_tag}"},
            "rules":generateRules(hyjack,domains,external_tag),
            "auto_detect_interface": bool("true")
            }        
