import json

#incarcam continut json
fisier = open('settings.json',"r")
parser = json.load(fisier)
print(parser['web-app']['servlet'][0]['init-param']['configGlossary:adminEmail'])

init_param = parser['web-app']['servlet'][0]['init-param']
init_param_keys = init_param.keys()
for key in init_param_keys:
    print("Key name = {}".format(key))