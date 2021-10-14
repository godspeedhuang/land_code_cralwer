import json

with open('test.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)

data_search = input("district_name：")
data_s = data[data_search]

with open(data_search+'.json', mode='w', encoding='utf-8') as file:
    json.dump(data_s, file)
