# -*- coding:utf8 -*-
import json
import time
import execjs
import requests

url = "https://www.ronghw.cn/api/visitor/eb/nonBid/compareList"

data = {"pageSize": 10, "pageNo": 4, "title": "", "projectCode": ""}
with open('招标.js', encoding='utf8') as f:
    sign_data = f.read()
headers = execjs.compile(sign_data).call('headers')

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)


"""
npm install crypto-js
"""