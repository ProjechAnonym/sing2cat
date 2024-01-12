from . import dnsPart,outPart,routePart
from config import GlobalVars
def generateConfig():
    keys = ['log','dns','inbounds','outbounds','route','experimental']
    values = [GlobalVars.getValues('log'),GlobalVars.getValues('dns'),GlobalVars.getValues('inbounds'),
              GlobalVars.getValues('outbounds'),GlobalVars.getValues('route'),GlobalVars.getValues('experimental')]
    config = dict(zip(keys,values))
    config['dns'] = dnsPart.dnsConfig()
    config['outbounds'] = outPart.outboundsConfig()
    config['route'] = routePart.routeConfig()
    return config