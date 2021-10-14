import requests
import json
import time

data = {"type": "FeatureCollection", "features": []}
inside = {"type": "Feature", "geometry": {"type": "MultiPolygon", "coordinates": [[]]}, "properties": {"縣市": "高雄市", "鄉鎮": "前鎮區", "地段": "經貿段一段", "段號": "", "id": "EC1048",
                                                                                                       "ymax": "", "ymin": "", "xmax": "", "xmin": "", "xcenter": "", "ycenter": "", "area_id": "EC", "section_id": "1048", "land_id": "", "query_log": [], "query": ""}}

code = 361334
for i in range(code, code+32):
    headers_m = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'G_ENABLED_IDPS=google; _ga_6VFQ37LNK6=GS1.1.1632902833.1.1.1632903993.0; cfid=990972a0-c6e0-4c37-a287-cab838c6ec02; cftoken=0; _gid=GA1.3.1736307411.1634033978; _ga=GA1.1.1907946975.1632403330; JSESSIONID=7DB162CCA8D55B1D432604FB33C623F7; _ga_QR16GVTCWQ=GS1.1.1634224612.3.0.1634224615.0',
        'Host': 'gisdawh.kcg.gov.tw',
        'Referer': 'https://gisdawh.kcg.gov.tw/landeasy/',
        'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'
    }
    form_data = {
        'where': 'OGR_FID='+str(i),
        'returnGeometry': 'true',
        'spatialRel': 'esriSpatialRelIntersects',
        'outFields': '*',
        'outSR': '102443'
    }
    request_url = 'https://gisdawh.kcg.gov.tw/landeasy/proxy/proxy2.ashx?https://mapgis2.kcg.gov.tw/server/rest/services/data/KCG_LANDEASY/MapServer/7/query?f=json'
    response = requests.get(request_url, data=form_data, headers=headers_m)
    elements = response.json()
    inside['geometry']['coordinates'][0].append(
        elements['features'][0]['geometry']['rings'][0])
    inside['properties']['land_id'] = elements['features'][0]['attributes']['AA49']
    data['features'].append(inside)
    print('success')
    time.sleep(5)

with open('test.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
