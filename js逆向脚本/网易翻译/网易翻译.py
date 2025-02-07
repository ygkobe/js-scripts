import requests
import datetime
import json
import hashlib
from urllib.parse import urlencode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64


def get_timestamp():
    return int(datetime.datetime.now().timestamp() * 1000)


def init_data():
    # 主要是获取key等参数
    url = "https://dict.youdao.com/webtranslate/key"
    mysticTime = get_timestamp()
    tmp_sign = f"client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key=asdjnjfenknafdfsdfsd"
    sign = hashlib.md5(tmp_sign.encode("utf8")).hexdigest()
    # 参数
    params = {
        'keyid': 'webfanyi-key-getter',
        'sign': sign,
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': mysticTime,
        'keyfrom': 'fanyi.web',
        'mid': 1,
        'screen': 1,
        'model': 1,
        'network': 'wifi',
        'abtest': '0',
        'yduuid': 'abcdefg',
    }

    url_with_params = f"{url}?{urlencode(params)}"

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://fanyi.youdao.com',
        'Pragma': 'no-cache',
        'Referer': 'https://fanyi.youdao.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"'
    }

    # 请求
    response = requests.get(url_with_params, headers=headers, data={})
    json_data = json.loads(response.text)
    # 获取 key

    return json_data['data']


def send(chinese):
    url = "https://dict.youdao.com/webtranslate"
    mysticTime = get_timestamp()
    data = init_data()
    aesIv = data['aesIv']
    aesKey = data['aesKey']
    secretKey = data['secretKey']
    # sign 是 client=fanyideskweb&mysticTime=1711295634744&product=webfanyi&key=fsdsogkndfokasodnaso
    tmp_sign = f"client=fanyideskweb&mysticTime={mysticTime}&product=webfanyi&key={secretKey}"
    sign = hashlib.md5(tmp_sign.encode("utf8")).hexdigest()

    payload = {
        'i': chinese,
        'from': 'auto',
        'to': '',
        'domain': '0',
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': sign,
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': mysticTime,
        'keyfrom': 'fanyi.web',
        'mid': 1,
        'screen': 1,
        'model': 1,
        'network': 'wifi',
        'abtest': '0',
        'yduuid': 'abcdefg',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1545431425@10.55.164.248; OUTFOX_SEARCH_USER_ID_NCOO=1617400304.3454392',
        'Origin': 'https://fanyi.youdao.com',
        'Pragma': 'no-cache',
        'Referer': 'https://fanyi.youdao.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.post(url, headers=headers, data=payload)

    encode_data = response.text
    # 开始解密数据
    # print("encode_data:", encode_data)
    # print("aesIv:", aesIv)
    # print("aesKey:", aesKey)
    decode(encode_data, aesIv, aesKey)


# 执行解密过程
def decode(encode_data, aesIv, aesKey):
    # 将秘密字符串转换为字节，并使用base64解码
    key = hashlib.md5(aesKey.encode('utf-8')).digest()
    iv = hashlib.md5(aesIv.encode('utf-8')).digest()
    # print(len(encode_data))

    # 解密数据
    # 创建AES解密器
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = aes.decrypt(base64.urlsafe_b64decode(encode_data))
    decrypted = unpad(decrypted_padded, AES.block_size).decode('utf8')

    # 返回解密后的数据
    json_data = json.loads(decrypted)
    print(json_data)

    #
    pass


if __name__ == '__main__':
    chinese = "你好"
    send(chinese)
