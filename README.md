# land_code_cralwer
- 抓地籍網站(有地理座標):
  - 全台：地號api https://twland.ronny.tw/
    （但資料更新為2015年前，有些地段已經消失或更名，加減用）
    - 程式碼 code_api.py
  - 高雄市：高雄地籍圖資服 https://gisdawh.kcg.gov.tw/landeasy/
    （透過土地資料查詢可以爬到geometry，但query_string沒有找到規則，要去一個對一下，比較適合少量地籍資料的抓取。）
    - 程式碼 crawler.py
    
- 基礎資料蒐集：
  - 全地號資料的蒐集:https://data.kcg.gov.tw/dataset/104-land-value-announcement/resource/ce676e39-e562-4c1d-b9b7-f80c4bba5fa3
 （高雄市政府資料開放平台／地政局／高雄市104年公告土地現值....檔案類型為csv） 
    1. 將欲蒐集地段之地號從csv寫成json格式
      - 程式碼 district.py
      - 檔案 地段名稱.json
    2. 將地號json丟進code_api.py裡面，從01010001寫成101-1格式，並丟入爬蟲取得geojson檔
      - 程式碼 code_api.json 
      - 檔案 地段名稱_地籍.json
