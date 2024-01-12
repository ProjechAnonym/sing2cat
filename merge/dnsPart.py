from config import GlobalVars
def getDnsList():
    if "dns_list" in GlobalVars.global_dict.keys():
        dns_list = GlobalVars.getValues("dns_list")
        return dns_list
    else:
        return False
def dnsServer(tag,dns):
    keys = ["tag","address",'address_strategy','strategy','detour']
    values = [tag,dns,'ipv4_only','prefer_ipv4',"select" if tag == "external" else "direct"]
    server = dict(zip(keys,values))
    return server
def dnsConfig():
    dns_list = getDnsList()
    if dns_list:
        internal_list = [dnsServer("internal",server) for server in dns_list["internal"]]
        external_list = [dnsServer("external",server) for server in dns_list["external"]]
        nodes_dns_list = [dnsServer("nodes_dns",server) for server in dns_list["nodes_dns"]]
        dns_servers = GlobalVars.getValues("dns")
        dns_servers["servers"] = internal_list + external_list + nodes_dns_list
        return dns_servers

    else:
        return GlobalVars.getValues("dns")