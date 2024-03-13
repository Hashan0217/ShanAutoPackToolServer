import asyncio

from automatedGitWorkFlow import autoMatedGitWorkFlow
from AutoReplacementAgreement import AutoReplacementAgreement
from requestModule import RequestModule

# 画一个GUI界面

class runApp:
    def __init__(self):
        self.filesPath = "E:/work/test"
        self.fileName = "target.json"
        self.headerConfig = {
            "brand": None,  # 自动循环生成
            "uniappid": "__UNI__FBA484B",
            "version": "1.0.0",
            "appname": "zhaochezhu",
            "phone-Brand": "",
            "sim": "0.0",
            "pack": "com.hc.findCar",
            "platform": "android",
        }
        self.PackagingplatformList = ["xiaomi", "oppo", "vivo", "huawei", "honor", "ali", "yingyongbao"]  #
        self.cureateAgreementData = {
            "companyName": "深圳市幻创文化有限公司",
            "appName": "找车主"
        }

    async def run(self):
        print('----------START----------')
        # 初始化git
        git = autoMatedGitWorkFlow(self.filesPath)
        index = 0
        for platform in self.PackagingplatformList:
            print('----------' + platform + '----------')
            if index == 0:
                git.gitInit()
                index += 1

            # 添加分支
            git.addBranch(platform)
            # 切换分支
            git.checkoutBranch(platform)

            # 请求头配置
            self.headerConfig["brand"] = platform
            url = 'https://hcom-test.xcjxcj.com'
            request = RequestModule(url, self.headerConfig)

            # 用户登录
            await request.userLogin()

            # 生成协议
            agreementRes = await request.createAgreement(self.cureateAgreementData)
            agreement = agreementRes['map']

            helpLink = agreement["helpUrl"]
            priLink = agreement["priUrl"]
            # 替换协议
            autoReplacementAgreement = AutoReplacementAgreement(self.filesPath, self.fileName, newHelpLink=helpLink, newPriLink=priLink)

            autoReplacementAgreement.__str__()
            autoReplacementAgreement.replacement_agreement()
            # 睡眠1秒
            await asyncio.sleep(1)
            # 提交代码
            git.autoCommit('autoCommit[协议更换]')
            print('--------END---------')





async def main():
    app = runApp()

    await app.run()


asyncio.get_event_loop().run_until_complete(main())
