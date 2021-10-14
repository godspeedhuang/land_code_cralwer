import requests
import json
import time
import random

land_name = input('請輸入段名:')
with open(land_name+'.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
with open('cantfindlandcode.json', mode='r', encoding='utf-8') as files:
    store = json.load(files)

new_list = []
for i in data:
    if i % 10000:
        a = i//10000
        b = i % 10000
        concat = str(a)+'-'+str(b)
        new_list.append(concat)
    else:
        a = i//10000
        new_list.append(str(a))

str_list = []
# t = len(new_list)//30
# s = len(new_list) % 30
count = 0
cantfind = list()
data = {"type": "FeatureCollection", "features": []}
for i in new_list:
    # try_list = list()
    # try_list = new_list[i*30-30:i*30-1]
    # for j in try_list:
    #     str1 = ('lands[]=高雄市', land_name, j)
    #     str2 = ','.join(str1)
    #     str_list.append(str2)
    # new_str = "&".join(str_list)
    request_url = 'https://twland.ronny.tw/index/search?lands[]='+"高雄市"+land_name+i+'號'
    response = requests.get(request_url)
    elements = response.json()
    if len(elements['features']) != 0:
        data['features'].append(elements['features'][0])
        count += 1
        print('success'+str(count))
    else:
        cantfind.append(i)
c_data = {land_name: cantfind}
store.append(c_data)

with open(land_name+'_地籍.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
with open('cantfindlandcode.json', mode='w', encoding='utf-8') as files:
    json.dump(store, files, ensure_ascii=False)
