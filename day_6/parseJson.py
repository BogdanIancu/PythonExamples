import json
json_string = '{"denumire" : "Pizza", "gramaj" : 300}'
parsed_json = json.loads(json_string)
print(parsed_json['denumire'])
print(parsed_json['gramaj'])

file = open('C:\\Users\\bogda\\Desktop\\Python\\PythonExamples\\day_6\\sample_files\\example.json',
mode ='r', buffering = True, encoding = 'utf-8')
parsed_json = json.load(file)

print(parsed_json['web-app']['taglib']['taglib-location'])
print(parsed_json['web-app']['servlet'][1])
print(parsed_json['web-app']['servlet'][1]['init-param']['mailHostOverride'])

file.close()