import pandas as pd
import json

data = pd.read_csv("104年公告地價.csv")

datas = dict()
district_name = []


for i, j in zip(data['地段名'], data['地號']):
    if i not in district_name:
        district_name.append(i)
        datas[i] = list()
        datas[i].append(j)
    else:
        datas[i].append(j)

with open('test.json', mode='w', encoding='utf-8') as file:
    json.dump(datas, file, ensure_ascii=False)
