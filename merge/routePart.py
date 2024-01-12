from config import GlobalVars
def formatRuleSet(ruleset,key):
    if ruleset['type'] == "local":
        rule_set = {'type':'local',"tag":key,'format':"binary","path":ruleset['path']}
    else:
        rule_set = {'type':'remote',"tag":key,'format':"binary","url":ruleset['url'],"download_detour": "select"}
    return rule_set
def getRuleSet():
    final_ruleset = GlobalVars.getValues('route')["rule_set"]
    custom_ruleset = GlobalVars.getValues("rule_set")
    if custom_ruleset:
        for key in custom_ruleset.keys():
            final_ruleset.append(formatRuleSet(custom_ruleset[key],key))
    return final_ruleset
def getRules():
    head_rules = GlobalVars.getValues('route')["rules"][:3]
    tail_rules = GlobalVars.getValues('route')['rules'][3:]
    custom_ruleset = GlobalVars.getValues("rule_set")
    if custom_ruleset:
        for key in custom_ruleset.keys():
            if custom_ruleset[key]['china']:
                head_rules.append({'rule_set':key,"outbound":"direct"})
            else:
                head_rules.append({'rule_set':key,"outbound":f"{key}-select"})
    head_rules.extend(tail_rules)
    return head_rules
def routeConfig():
    origin_route_config = GlobalVars.getValues('route')
    origin_route_config['rule_set'] = getRuleSet()
    origin_route_config['rules'] = getRules()
    return origin_route_config
