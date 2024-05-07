import asyncio
from time import sleep
from automatedGitWorkFlow import autoMatedGitWorkFlow
from AutomatiCallyReplaceText import AutomaticallyReplaceText
from requestModule import RequestModule
from autoPackModule import autoPack
from AutoMaticallReplaceVue import VueFileHandler
# 画一个GUI界面

class runApp:
    def __init__(self):
        self.filesPath = "E:\work\identification"
        self.fileName = "androidPrivacy.json"
        self.headerConfig = {
            "brand": None,  # 自动循环生成
            "uniappid": "__UNI__F6780F5",
            "version": "1.0.0",
            "appname": "zhaopianhuifushi",
            "phone-Brand": "xiaomi",
            "sim": "0.0",
            "pack": "dou.yin.one",
            "platform": "android",
        }
        self.PackagingplatformList = ["vivo"]
        self.cureateAgreementData = {
            "companyName": "深圳市幻创文化有限公司",
            "appName": "照片恢复师"
        }


    async def run(self):

        print('----------START----------')
        # 初始化git
        git = autoMatedGitWorkFlow(self.filesPath)
        index = 0
        for platform in self.PackagingplatformList:
            print('----------' + platform + '----------')

            # 特殊配置
            platfromTemp = platform.split('-')[0]

            if index == 0:
                git.gitInit()

            # 查看分支是否存在
            if git.is_branch_exists(platform):
                # 切换分支
                git.checkoutBranch(platform)
            else:
                # 添加分支
                git.addBranch(platform)
                # 切换分支
                git.checkoutBranch(platform)

            # 请求头配置
            self.headerConfig["brand"] = platfromTemp
            url = 'https://hcom.xcjxcj.com' #https://hcom-test.xcjxcj.com
            request = RequestModule(url, self.headerConfig)

            # 用户登录
            await request.userLogin()

            # 生成协议
            agreementRes = await request.createAgreement(self.cureateAgreementData)
            agreement = agreementRes['map']

            helpLink = agreement["helpUrl"]
            priLink = agreement["priUrl"]
            # 替换协议
            autoReplaceText = AutomaticallyReplaceText(self.filesPath, self.fileName, newHelpLink=helpLink, newPriLink=priLink)

            autoReplaceText.__str__()
            autoReplaceText.replacement_agreement()



            # 替换平台名称
            # 创建 VueFileHandler 实例
            vue_file_path = self.filesPath + '/App.Vue'
            vue_handler = VueFileHandler(vue_file_path)



            # 修改 Vue 文件
            if index == 0:
                search_string = "oppo"
                replacement_string = platfromTemp
                vue_handler.modify_vue_file(search_string, replacement_string)
            else:
                search_string = self.PackagingplatformList[index-1].split('-')[0]
                replacement_string = self.PackagingplatformList[index].split('-')[0]
                vue_handler.modify_vue_file(search_string, replacement_string)

            git.autoCommit('autoCommit[替换协议+平台名称]')
            index += 1
            sleep(3)

            # # 打包
            # pack = autoPack()
            # isOk = await pack.run(project='identification', channels=platfromTemp, path=self.filesPath+'/packConfig.json')
            #
            # if isOk:
            #     print('----------工作流成功----------')
            #
            # else:
            #     print('----------工作流失败----------')
            #     break
            #
            # # 睡眠1秒
            # await asyncio.sleep(1)
            # # 提交代码
            # git.autoCommit('autoCommit[打包完成]')
            # print('--------END---------')



async def main():
    app = runApp()

    await app.run()


asyncio.get_event_loop().run_until_complete(main())
