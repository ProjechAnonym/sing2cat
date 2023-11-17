import re
def FormatCheck(hostlist):
    single_host = re.split("\n",hostlist)
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
def processHOST(host):
    domains = [None]*len(host)
    IPs = [None]*len(host)
    Ports = [None]*len(host)
    for i in range(len(host)):
        info = re.split(",|，",host[i])
        domains[i] = info.copy()[0]
        IPs[i] = info.copy()[1]
        Ports[i] = int(info.copy()[2])
    return [domains,IPs,Ports]
        