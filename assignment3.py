#coding=utf-8
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)
attraction_list=data["result"]["results"]

def file_split(file_string):
    # 用https來做分割
    all_file = file_string.split("https:")
    # 取list中的第二個元素，再把前面的"https"加回去，並將"/d_upload_ttn/sceneadmin/"去除
    first_file = "https:" + all_file[1].replace("/d_upload_ttn/sceneadmin", "")
    return first_file

with open("data.csv", "w", encoding="utf-8") as file:
    for i in range (0, len(attraction_list)):
        if attraction_list[i]["xpostDate"][0:4] >= "2015":
            file.write(attraction_list[i]["stitle"] + "," + attraction_list[i]["address"][5:8] + "," + attraction_list[i]["longitude"] + "," + attraction_list[i]["latitude"]+ "," + file_split(attraction_list[i]["file"])+ "\n")

"""
景點名稱 stitle
區域 address
經度 longitude
緯度 latitude
第一張圖檔網址 file
景點時間 xpostDate
"""