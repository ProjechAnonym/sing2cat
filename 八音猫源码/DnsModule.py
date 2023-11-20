def DNSserver(DNS_list):
    return [{
        "tag": "external",
        "address": f"{DNS_list[0]}",
        "address_strategy": "ipv4_only",
        "strategy": "prefer_ipv4",
        "detour": "select"
      },
      {
        "tag": "proxy_search",
        "address": f"{DNS_list[1]}",
        "address_strategy": "ipv4_only",
        "strategy": "prefer_ipv4",
        "detour": "direct"
      },
      {
        "tag": "internal",
        "address": f"{DNS_list[2]}",
        "address_strategy": "ipv4_only",
        "strategy": "prefer_ipv4",
        "detour": "direct"
      },
      {
        "tag": "dns_block",
        "address": "rcode://refused"
      }]
def DNScache(ttl):
    return [
      {
        "geosite": ["category-ads-all"],
        "server": "dns_block",
        "disable_cache": True
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
def DNSjson(dns_list,ttl):
    return {"servers":DNSserver(dns_list),
                "rules":DNScache(ttl),
                "strategy": "prefer_ipv4",
                "final": "external",
                "disable_cache": False,
                "disable_expire": False,
                "independent_cache": False,
                "reverse_mapping": False}