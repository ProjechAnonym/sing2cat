def Outbounds(ips,ports):
    destinations_list = []
    for ip_port in range(len(ips)):
        destinations_list.append(f'{ips[ip_port]}:{ports[ip_port]}')
    destinations_set = set(destinations_list)
    destinations_key = list(destinations_set)
    outbound = dict.fromkeys(destinations_key,0)
    index = 1
    for key in outbound.keys():
        outbound[key] = index
        index = index + 1
    return outbound