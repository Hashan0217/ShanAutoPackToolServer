import os
import subprocess
import asyncio
import json

class autoPack:
    def __init__(self):
        self.packConfig = None

    async def setPackConfig(self, project, platform, iscustom, safemode, packagename, androidpacktype, certalias, certfile, certpassword, channels, isconfusion, splashads, rpads, pushads, exchange,configJosnPath):
        self.packConfig = {
            "project": project,
            "platform": platform,
            "iscustom": iscustom,
            "safemode": safemode,
            "android": {
                "packagename": packagename,
                "androidpacktype": androidpacktype,
                "certalias": certalias,
                "certfile": certfile,
                "certpassword": certpassword,
                "channels": channels
            },
            "isconfusion": isconfusion,
            "splashads": splashads,
            "rpads": rpads,
            "pushads": pushads,
            "exchange": exchange
        }
        self.configJosnPath = configJosnPath
        await self.writeJsonFile(self.packConfig)
        await asyncio.sleep(3)
        return self.packConfig

    async def writeJsonFile(self, data):
        with open(self.configJosnPath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    async def cilPack(self, config_path):
        os.chdir('D:/HBuilderX')
        terminal = await asyncio.create_subprocess_shell("cmd", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        terminal.stdin.write(b"cli.exe open\n")
        await terminal.stdin.drain()

        await asyncio.sleep(1)

        terminal.stdin.write(f"cli pack --config {config_path}\n".encode())
        await terminal.stdin.drain()

        resData = None

        while True:
            isOk = await self.monitor_output(terminal)
            if isOk:
                print("打包成功")
                resData = True
                break
            if isOk == -1:
                print("打包失败")
                resData = False
                break

        return resData

    async def monitor_output(self, terminal):
        while True:
            try:
                output = (await terminal.stdout.readline()).decode('gbk').strip()
            except UnicodeDecodeError:
                output = "UnicodeDecodeError occurred, cannot decode the output"
            if output:
                print("Terminal Output:", output)
                if "是否继续提交" in output:
                    print("Cancelling the task...")
                    terminal.stdin.write(b"\n")
                    print('同意')
                if "打包成功" in output and "安装包位置" in output:
                    print("打包成功")
                    return True
                if "打包失败" in output:
                    print("打包失败")
                    return -1
                if "不存在" in output:
                    print("打包失败")
                    return -1
            else:
                print('--没有输出--')
                break


    #
    async def run(self, project='identification', platform='android', iscustom=False, safemode=True, packagename='com.Illusory.zjz', androidpacktype=1, certalias='com.Illusory.zjz', certfile='E:/证书文件/证件照_com.Illusory.zjz/安卓/com.Illusory.zjz.keystore', certpassword='123456', channels='', isconfusion=False, splashads=False, rpads=False, pushads=False, exchange=False, path=None):
        await self.setPackConfig(project, platform, iscustom, safemode, packagename, androidpacktype, certalias, certfile, certpassword, channels, isconfusion, splashads, rpads, pushads, exchange,configJosnPath=path)
        await asyncio.sleep(2)
        return await self.cilPack(path)





















# import os
# import subprocess
# import time
# import json
# class autoPack:
#     def __init__(self):
#         self.packConfig = None
#
#     # 设置打包配置
#     # project 项目绝对路径
#     # platform 打包平台 默认值android  值有"android","ios" 如果要打多个逗号隔开打包平台
#     # iscustom 是否使用自定义基座 默认值False  true自定义基座 False自定义证书
#     # safemode 打包方式是否为安心打包默认值False,true安心打包,False传统打包
#     # packagename 安卓包名
#     # androidpacktype 安卓打包类型 默认值0 0 使用自有证书 1 使用公共证书 2 使用老版证书
#     # certalias 安卓打包证书别名,自有证书打包填写的参数
#     # certfile 安卓打包证书文件路径,自有证书打包填写的参数
#     # certpassword 安卓打包证书密码,自有证书打包填写的参数
#     # channels 安卓平台要打的渠道包 取值有"google","yyb","360","huawei","xiaomi","oppo","vivo"，如果要打多个逗号隔开
#     # isconfusion 是否混淆 true混淆 False关闭
#     # splashads 开屏广告 true打开 False关闭
#     # rpads 悬浮红包广告true打开 False关闭
#     # pushads push广告 true打开 False关闭
#     # exchange 加入换量联盟 true加入 False不加入
#
#     def setPackConfig(self, project, platform, iscustom, safemode, packagename, androidpacktype, certalias, certfile, certpassword, channels, isconfusion, splashads, rpads, pushads, exchange):
#         self.packConfig = {
#             # 项目名字或项目绝对路径
#             "project": project,
#             # 打包平台 默认值android  值有"android","ios" 如果要打多个逗号隔开打包平台
#             "platform": platform,
#             # 是否使用自定义基座 默认值False  true自定义基座 False自定义证书
#             "iscustom": iscustom,
#             # 打包方式是否为安心打包默认值False,true安心打包,False传统打包
#             "safemode": safemode,
#             # android打包参数
#             "android": {
#               # 安卓包名
#               "packagename": packagename,
#               # 安卓打包类型 默认值0 0 使用自有证书 1 使用公共证书 2 使用老版证书
#               "androidpacktype": androidpacktype,
#               # 安卓使用自有证书自有打包证书参数
#               # 安卓打包证书别名,自有证书打包填写的参数
#               "certalias": certalias,
#               # 安卓打包证书文件路径,自有证书打包填写的参数
#               "certfile": certfile,
#               # 安卓打包证书密码,自有证书打包填写的参数
#               "certpassword": certpassword,
#               # 安卓平台要打的渠道包 取值有"google","yyb","360","huawei","xiaomi","oppo","vivo"，如果要打多个逗号隔开
#               "channels": channels
#               },
#             # 是否混淆 true混淆 False关闭
#             "isconfusion": isconfusion,
#             # 开屏广告 true打开 False关闭
#             "splashads": splashads,
#             # 悬浮红包广告true打开 False关闭
#             "rpads": rpads,
#             # push广告 true打开 False关闭
#             "pushads": pushads,
#             # 加入换量联盟 true加入 False不加入
#             "exchange": exchange
#         }
#         # 生成json文件 命名为packConfig.json
#         self.writeJsonFile(self.packConfig)
#         return self.packConfig
#
#     # 生成文件
#     def writeJsonFile(self, data, path):
#
#         # 编码方式 UTF-8
#         with open(path, 'w', encoding='utf-8') as f:
#             json.dump(data, f, ensure_ascii=False)
#         return True
#
#     # cil打包
#     def cilPack(self,config_path):
#         # 切换到指定目录
#         os.chdir('D:/HBuilderX')
#
#         # 打开终端并保持连接
#         terminal = subprocess.Popen(["cmd"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                                     shell=True)
#
#         # 向终端发送命令
#         terminal.stdin.write(b"cli.exe open\n")
#         terminal.stdin.flush()
#
#         # 等待一段时间，以确保打开操作完成
#         time.sleep(1)
#         # terminal.stdin.write(b"cli pack --config e:/temppp/tempCarrr/packConfig.json\n")
#         terminal.stdin.write(f"cli pack --config {config_path}\n".encode())
#         terminal.stdin.flush()
#
#         resData = None
#
#         # 循环监听输出
#         while True:
#             isOk = self.monitor_output(terminal)
#             if isOk:
#                 print("打包成功")
#                 resData = True
#                 break
#             if isOk == -1:
#                 print("打包失败")
#                 resData = False
#                 break
#
#
#         return  resData
#
#     # 监听终端输出
#     def monitor_output(self, terminal):
#         while True:
#             try:
#                 output = terminal.stdout.readline().decode('gbk').strip()
#             except UnicodeDecodeError:
#                 output = "UnicodeDecodeError occurred, cannot decode the output"
#             if output:
#                 print("Terminal Output:", output)
#                 if "是否继续提交" in output:
#                     print("Cancelling the task...")
#                     terminal.stdin.write(b"cli.exe cancel\n")  # Send command to cancel the task
#                     terminal.stdin.flush()
#                 if "打包成功" in output:
#                     print("打包成功")
#                     return True
#                 if "打包失败" in output:
#                     print("打包失败")
#                     return -1
#             else:
#                 print('--没有输出--')
#                 break
#
#     # 运行
#     def run(self, project, platform, iscustom, safemode, packagename, androidpacktype, certalias, certfile, certpassword, channels, isconfusion, splashads, rpads, pushads, exchange, path):
#         packConfig = self.setPackConfig(project='tempCarrr', platform='android', iscustom=False, safemode=True, packagename='com.hc.findCar', androidpacktype=1, certalias='com.hc.findCar', certfile='e:/证书文件/找车主/安卓/com.hc.findCar.keystore', certpassword='123456', channels='huawei', isconfusion=False, splashads=False, rpads=False, pushads=False, exchange=False)
#         self.writeJsonFile(packConfig, path)
#         time.sleep(5)
#         self.cilPack(path)
#
#
#
