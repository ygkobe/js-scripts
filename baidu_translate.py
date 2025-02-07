# -*- coding:utf8 -*-
import time
import execjs
import requests

url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

query = "我是马嘉祺"
with open('baidu_translate.js', encoding='utf8') as f:
    sign_data = f.read()
query_data = execjs.compile(sign_data).call('sign', query)


data = {
    "from": "zh",
    "to": "en",
    "query": query,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": query_data,
    "token": "fe72cfe3239980b2833e76baf3b6f426",
    "domain": "common",
    "ts": str(time.time())
}

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "acs-token": "1737713021744_1737982687420_vcAaUct1Ubraxnouv6MJbGSlkKu18PgeI5JSz6Qc4dFnmi7uBo9mRKsgco4rhJruGvd0dHHlmGsGP9pyY+PUfvNLcsmwY5o3wY5Dbq+2Dx7bEYAdULEYoZOrM37TzK3pcqlgEPreFTRaWveoFgg/i9sjvdogXGk7oI9BaTm++l7zgxfZqN/8TrBt38VQDcEBaXmhLkCVviWrBj3alOCNAr85X3V3DTUdUePKg4/ZDpGAvHg+ePGLEk2+wn1b8Z4Ww+OPmVnWZFn8L3W5ep45YEwSmaG6n+qY/860Mid+5lHlR8aA4xo8GKiAO0cFZcjYfnVoaDJNlGbZ08B2WtOXYTI4ptdl+3iVIKH9gMZ59d3WwvYLm9qqTwObPDT1bH8yDt2tz5fmpnP5yaJ/H/O/vYQ48dIznvDqR6fK/pasW1ZTXGDSY71oJJk3+dBUCkcJmYAMOcJ9/G1srzfQBezOeD0qzpAt4OOaODQukyOUU8OLM3QnUOj/ptrF30/Tfl06",
    "connection": "keep-alive",
    "content-length": "184",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "smallFlowVersion=old; BAIDUID=2D3527C80762DB8CAC194D9BAA63CA3C:FG=1; PSTM=1724678370; BIDUPSID=DBC5BF75912286307E0123C510417A12; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MAWEBCUID=web_wsQUnTOuGesQPopdqljBotJMPfbNtArGesgkIBPoJRbfvclqvR; H_WISE_SIDS_BFESS=110085_633619_633567_636043_636326_636788_637300_637699_637731_637770_637773_636303_638383; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1736849491,1737018344,1737098710,1737254704; HMACCOUNT=15CC1FE2E9E498EC; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=I7IOJexroGWU6LJJuMdO77ATlrGQd7cTDYrEOwXPsp3LGJLVdPjFEG0PtOUBxFP-oxShogKKKeOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JRktoIPXJI-3JbTkbP7hhICbblrt2D62aJ0LLPbvWJ5TMCo6MRr4-nKpMJ3BKnoOWN63oUna3nk-ShPCb6bTbRkf0Pcn-55qJD5J0P_M3l02VKQIe-t2yUKJyP5a--RMW20jWl7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJ9jjCajTcQjG8Oqbbfb-oKQPJs56rjDnCk-PI33tTQXP6-hnjy3avP_qRFWfcOEJ86jUQxhbD10f8f5h3Ry6r4bPbtH45KKfbzQUO4bh8qQ4oxJpOJBaTGXpQxHR7WVnnvbURvyPLg3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoKDyfIP2bKLrKPoVqRkt-fn-eR3-KK-X3b7Efb68Eq7_bf--DRLWhh5btxTzMtjT_K3pQn4bEtLwy46xy5K_hNo73bopJ6vwWx5-2bTfsP5HQT3m-xrbbN3itPjLtGFfWb3cWKJV8UbSjxRPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50eGKHt6KtJbutVbobHJoHjJbGq4bohjPpyMR9BtQO-DOx-brwt-oko4Fzh6tbLq0jhtRi243HQgnkQq5vbMnmqPtRXMJkXhK4XJDq0x-jLTPOB66na-5DVJQOhtnJyUPUbtnnBT5i3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CFhJKI2MC-9eP55q4D_MfOtetJyaR3A_hTvWJ5WqR7j3p_-XMIp5tcbW5-f0GnQQq3l5I3jShbXKxoc5pkrKp0eWUbZBNcbbncI3l02V-bO3f5WQlODhp7gaPRMW23i0l7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjj6jK4JKjG_jq6QP; H_PS_PSSID=61027_61781_61873_61889_61985; delPer=0; PSINO=1; BAIDUID_BFESS=2D3527C80762DB8CAC194D9BAA63CA3C:FG=1; BDSFRCVID_BFESS=I7IOJexroGWU6LJJuMdO77ATlrGQd7cTDYrEOwXPsp3LGJLVdPjFEG0PtOUBxFP-oxShogKKKeOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=JRktoIPXJI-3JbTkbP7hhICbblrt2D62aJ0LLPbvWJ5TMCo6MRr4-nKpMJ3BKnoOWN63oUna3nk-ShPCb6bTbRkf0Pcn-55qJD5J0P_M3l02VKQIe-t2yUKJyP5a--RMW20jWl7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJ9jjCajTcQjG8Oqbbfb-oKQPJs56rjDnCk-PI33tTQXP6-hnjy3avP_qRFWfcOEJ86jUQxhbD10f8f5h3Ry6r4bPbtH45KKfbzQUO4bh8qQ4oxJpOJBaTGXpQxHR7WVnnvbURvyPLg3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoKDyfIP2bKLrKPoVqRkt-fn-eR3-KK-X3b7Efb68Eq7_bf--DRLWhh5btxTzMtjT_K3pQn4bEtLwy46xy5K_hNo73bopJ6vwWx5-2bTfsP5HQT3m-xrbbN3itPjLtGFfWb3cWKJV8UbSjxRPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50eGKHt6KtJbutVbobHJoHjJbGq4bohjPpyMR9BtQO-DOx-brwt-oko4Fzh6tbLq0jhtRi243HQgnkQq5vbMnmqPtRXMJkXhK4XJDq0x-jLTPOB66na-5DVJQOhtnJyUPUbtnnBT5i3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CFhJKI2MC-9eP55q4D_MfOtetJyaR3A_hTvWJ5WqR7j3p_-XMIp5tcbW5-f0GnQQq3l5I3jShbXKxoc5pkrKp0eWUbZBNcbbncI3l02V-bO3f5WQlODhp7gaPRMW23i0l7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjj6jK4JKjG_jq6QP; ZFY=i8I:AZRfRBO0jbeq6XkzupCXfbAcm2xdqgX8:B6S4BjzI:C; H_WISE_SIDS=61027_61781_61873_61889_61985; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1737903196",
    "host": "fanyi.baidu.com",
    "origin": "https://fanyi.baidu.com",
    "referer": "https://fanyi.baidu.com/?fr=pcPinzhuan",
    "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

response = requests.post(url=url, headers=headers, data=data)
print(response.text)