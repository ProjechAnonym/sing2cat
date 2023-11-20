import re
def FormatCheck(host_list):
    single_host = re.split("\n",host_list)
    hosts = [True]
    for i in single_host:
        if i == "":
            continue
        elif len(re.split(',|，',i)) == 3:
            for j in re.split(',|，',i):
                if j != "":
                    continue
                else:
                    return [False,i]
            hosts.append(i)
            continue
        else:
            return [False,i]
    return hosts
def ProcessHost(hosts):
    domains = [None]*len(hosts)
    IPs = [None]*len(hosts)
    Ports = [None]*len(hosts)
    for i in range(len(hosts)):
        info = re.split(",|，",hosts[i])
        domains[i] = info.copy()[0]
        IPs[i] = info.copy()[1]
        Ports[i] = int(info.copy()[2])
    return [domains,IPs,Ports]
        