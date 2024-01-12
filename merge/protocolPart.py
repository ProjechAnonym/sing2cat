from config import GlobalVars
import re
def formatTag(node_name):
    countries = GlobalVars.getValues('country')
    for index,country in enumerate(countries):
        if re.search(country,node_name):
            country_count = GlobalVars.getValues(country)
            if country_count:
                name = f"{country}-{country_count + 1}"
                GlobalVars.setValues(country,country_count + 1)
            else:
                name = f"{country}-1"
                GlobalVars.setValues(country,1)
            break
        else:
            if index == len(countries) - 1:
                unknown_count = GlobalVars.getValues(countries[index])
                if unknown_count:
                    name = f"{countries[index]}-{unknown_count + 1}"
                    GlobalVars.setValues(countries[index],unknown_count + 1)
                else:
                    name = f"{countries[index]}-1"
                    GlobalVars.setValues(countries[index],1)
    return name
def vmess(node):
    vmess = GlobalVars.getValues('outbounds')['vmess']
    vmess['tag'] = formatTag(node['name'])        
    vmess['server'] = node['server']
    vmess['server_port'] = int(node['port'])
    vmess['uuid'] = node['uuid']
    vmess['transport']['type'] = node['network']
    vmess['transport']['path'] = node['ws-path']
    vmess['transport']['headers'] = node['ws-headers']
    return vmess
def shadowsocks(node):
    ss = GlobalVars.getValues('outbounds')['ss']
    ss["tag"] = formatTag(node["name"])
    ss["server"] = node["server"]
    ss["server_port"] = int(node["port"])
    ss["method"] = node["cipher"]
    ss["password"] = node["password"]
    return ss
def trojan(node):
    trojan = GlobalVars.getValues('outbounds')['trojan']   
    trojan["tag"] = formatTag(node["name"])
    trojan["server"] = node["server"]
    trojan["server_port"] = int(node["port"])
    trojan["password"] = node["password"]
    trojan["tls"]["server_name"] = node["sni"]
    return trojan