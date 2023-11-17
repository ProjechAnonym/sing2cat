def serverSwitch(internal,external,proxy_search,external_tag):
    return [{
        "tag": "external",
        "address": f"{external}",
        "address_strategy": "ipv4_only",
        "strategy": "prefer_ipv4",
        "detour": external_tag
      },
      {
        "tag": "proxy_search",
        "address": f"{proxy_search}",
        "address_strategy": "ipv4_only",
        "strategy": "prefer_ipv4",
        "detour": "direct"
      },
      {
        "tag": "internal",
        "address": f"{internal}",
        "address_strategy": "ipv4_only",
        "strategy": "prefer_ipv4",
        "detour": "direct"
      },
      {
        "tag": "dns_block",
        "address": "rcode://refused"
      }]
def dnsRules(ttl):
    return [
      {
        "geosite": ["category-ads-all"],
        "server": "dns_block",
        "disable_cache": bool("true")
      },
      { "outbound": "any", "server": "proxy_search" },
      {
        "geosite": ["cn", "private"],
        "server": "internal",
        "rewrite_ttl": ttl
      },
      {
        "geosite": ["geolocation-!cn"],
        "server": "external",
        "rewrite_ttl": ttl
      }
    ]
def dnsOut(internal,external,proxy_search,ttl,external_tag):
    return {"servers":serverSwitch(internal,external,proxy_search,external_tag),
                "rules":dnsRules(ttl),
                "strategy": "prefer_ipv4",
                "final": "external",
                "disable_cache": bool(None),
                "disable_expire": bool(None),
                "independent_cache": bool(None),
                "reverse_mapping": bool(None)}