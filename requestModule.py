import json

import requests

class RequestModule:
    def __init__(self, url, headersConfig):
        self.url = url
        self.headersConfig = headersConfig
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "brand":  self.headersConfig["brand"],
            "uniappid": self.headersConfig["uniappid"],
            "version": self.headersConfig["version"],
            "appname": self.headersConfig["appname"],
            "phone-Brand": self.headersConfig["brand"],
            "sim": self.headersConfig["sim"],
            "pack": self.headersConfig["pack"],
            "platform": self.headersConfig["platform"],
        }

        self.token = None
    # 发送网络请求
    def request(self, pathUrl, method, data=None):
        url = self.url + pathUrl

        if method == "GET":
            response = requests.get(url=url, headers=self.headers)
        elif method == "POST":
            json_data = json.dumps(data)
            response = requests.post(url=url, data=json_data, headers=self.headers)

        return json.loads(response.text)

    # 用户登录
    def userLogin(self):
        pathUrl = "/app-auth/login"
        data = {
                "phone": "adfgdfdgfdfgdshjkl",
                "password": "Bj322PFO39zE7mRHquh/hhLFdzuAfF9l+THMfANWZrt+YRcrXD5G1bgTse2dRdcyTtU/P8S1I9M59rvnh5bRfGRVaYkeJs2WxNeBNIDTUxcLoNDGM4ozZ/4++zU2+W/4Pq8fuahLtVhfMa1hWSzXkK8oVlEXMli3eXorcLZUCAA=",
                "loginType": -1,
                "device": "adfgdfdgfdfgdshjkl",
            }
        res = self.request(pathUrl, "POST", data=data)
        # 获取token的值
        token = res['data']['token']
        self.headers["token"] = token
        # self.token = token
        # print(token)

    # 生成协议
    def createAgreement(self):
        data = {
            "companyName": "深圳市幻创文化有限公司",
            "appName": "运势测算"
        }
        res = self.request("/app-deal/general", "POST", data=data)
        agreement = res['map']
        return agreement





haderConfig = {
    "brand": "xiaomi",
    "uniappid": "__UNI__151D0F6",
    "version": "1.0.4",
    "appname": "hanshizhengjianzhao",
    "phone-Brand": "",
    "sim": "0.0",
    "pack": "com.photo.yy",
    "platform": "android",
    "device": ",,",
}
test = RequestModule("https://hcom-test.xcjxcj.com", haderConfig)
test.userLogin()
test.createAgreement()