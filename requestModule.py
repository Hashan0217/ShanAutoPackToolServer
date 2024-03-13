import json
import asyncio
import aiohttp
import requests

class RequestModule:
    def __init__(self, url, header_config):
        self.url = url
        self.header_config = header_config
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "brand":  self.header_config["brand"],
            "uniappid": self.header_config["uniappid"],
            "version": self.header_config["version"],
            "appname": self.header_config["appname"],
            "phone-Brand": self.header_config["brand"],
            "sim": self.header_config["sim"],
            "pack": self.header_config["pack"],
            "platform": self.header_config["platform"],
        }

        self.token = None


    # 用户登录
    async def userLogin(self):
        print('用户登录开始')
        pathUrl = self.url + "/app-auth/login"
        data = {
            "phone": "adfgdfdgfdfgdshjkl",
            "password": "Bj322PFO39zE7mRHquh/hhLFdzuAfF9l+THMfANWZrt+YRcrXD5G1bgTse2dRdcyTtU/P8S1I9M59rvnh5bRfGRVaYkeJs2WxNeBNIDTUxcLoNDGM4ozZ/4++zU2+W/4Pq8fuahLtVhfMa1hWSzXkK8oVlEXMli3eXorcLZUCAA=",
            "loginType": -1,
            "device": "adfgdfdgfdfgdshjkl",
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(pathUrl, json=data, headers=self.header_config) as response:
                res = await response.json()
                self.token = res['data']['token']
                print('用户登录结束')

    # 生成协议
    async def createAgreement(self, data):
        print('生成协议开始')
        data = data
        pathUrl = self.url + "/app-deal/general"
        async with aiohttp.ClientSession() as session:
            async with session.post(pathUrl, json=data, headers=self.header_config) as response:
                print('生成协议结束')
                return await response.json()




