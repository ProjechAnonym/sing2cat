import json,os,sys,re,yaml
def formatUrl():
    for index,url in enumerate(global_dict['url']):
        args = re.split(r'\?|&',url)
        for arg in args:
            clash_tag = True if re.search('clash',arg) else False
        if not clash_tag:
            global_dict["url"][index] = url + "&flag=clash"
def initGlobalVars():
    global global_dict
    global_dict = {}
    base_dir = os.path.dirname(sys.argv[0])
    with open(os.path.join(base_dir,'static/template.json'),mode='r',encoding='utf-8') as f:
        template_content = json.loads(f.read())
    with open(os.path.join(base_dir,'static/config.json'),mode='r',encoding='utf-8') as f:
        config_content = json.loads(f.read())
    with open(os.path.join(base_dir,'static/country.yaml'),mode='r',encoding='utf-8') as f:
        country_content = yaml.load(f.read(),yaml.BaseLoader)
    country_content_keys_num = len(country_content.keys())
    template_content_keys_num = len(template_content.keys())
    config_content_keys_num = len(config_content.keys())
    keys = [None] * (template_content_keys_num + config_content_keys_num + country_content_keys_num)
    values = [None] * (template_content_keys_num + config_content_keys_num + country_content_keys_num)
    for index,key in enumerate(template_content.keys()):
        keys[index] = key
        values[index] = template_content[key]
    for index,key in enumerate(config_content.keys()):
        keys[index + template_content_keys_num] = key
        values[index + template_content_keys_num] = config_content[key]
    for index,key in enumerate(country_content.keys()):
        keys[index + template_content_keys_num + config_content_keys_num] = key
        values[index + template_content_keys_num + config_content_keys_num] = country_content[key]
    global_dict = dict(zip(keys,values))
    formatUrl()
def setValues(key,value):
    global_dict[key] = value
def getValues(key):
    try:
        return global_dict[key]
    except Exception as e:
        if key in global_dict['country']:
            pass
        else:
            print(f"索引出错,{e}")

    

    