# -*- coding:utf8 -*-
import time
import json
import execjs
import requests

url = "https://capi.jiansheku.com/nationzj/jskBid/page"

with open('建筑工程招标.js', encoding='utf8') as f:
    js_data = f.read()
request_data = execjs.compile(js_data).call('sign', 1)

payload = request_data.get('payload')
timestamp = request_data.get('timestamp')
sign = request_data.get('sign')

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "content-length": "243",
    "content-type": "application/json",
    "cookie": "Hm_lvt_03b8714a30a2e110b8a13db120eb6774=1744872173,1745197628,1745285370; Hm_lpvt_03b8714a30a2e110b8a13db120eb6774=1745285370; HMACCOUNT=168C34E424DAA4C8",
    "devicetype": "PC",
    "origin": "https://www.jiansheku.com",
    "priority": "u=1, i",
    "referer": "https://www.jiansheku.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sign": sign,
    "timestamp": str(timestamp),
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}


response = requests.post(url=url, headers=headers, data=json.dumps(payload))
print(response.text)