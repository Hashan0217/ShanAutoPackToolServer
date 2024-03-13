import os
import json
import re



class AutoReplacementAgreement:
    def __init__(self, path, filename,newHelpLink,newPriLink):
        self.path = path
        self.filename = filename
        self.targetFile = None
        self.fileContent = None
        self.newHelpLink = newHelpLink
        self.newPriLink = newPriLink

    def __str__(self):
        self.find_files(self.filename)
    # 列出文件目录
    def list_files(self):
        files = os.listdir(self.path)
        return files

    # 根据目录查找指定文件 用递归
    def find_files(self, filename):
        def inner_find_files(path):
            files = self.list_files()
            for file in files:
                if os.path.isdir(path + '/' + file):
                    inner_find_files(path + '/' + file)
                elif file == filename:
                    self.targetFile = path + '/' + file
                    return

        inner_find_files(self.path)

    # 替换链接
    def replace_links(self, message, pattern):
        # 匹配message中的链接
        matches = re.findall(pattern, message)
        for match in matches:
            href = match[0]
            text = match[1]
            if "help" in href:
                message = message.replace(href, self.newHelpLink)
            elif "pri" in href:
                message = message.replace(href, self.newPriLink)

        return message

    # 更换协议
    def replacement_agreement(self):
        print('协议更换开始')
        # 根据 targetFile 读取 JSON 文件内容
        with open(self.targetFile, 'r', encoding='utf-8') as file:
            fileContent = json.load(file)
            pattern = r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>'
            message = fileContent["message"]
            second_message = fileContent["second"]["message"]

            messageRes = self.replace_links(message, pattern)
            second_messageRes = self.replace_links(second_message, pattern)

            fileContent["message"] = messageRes
            fileContent["second"]["message"] = second_messageRes

            self.fileContent = fileContent
            print('协议更换完成')

            self.generate_json()
            # print(fileContent)


    # 根据文字替换内容
    def replace_text(self, search_string, replacement_string):
        print('文字更换开始')
        with open(self.targetFile, 'r', encoding='utf-8') as file:
            fileContent = json.load(file)
            # 将对象转换为字符串
            json_str = json.dumps(fileContent, ensure_ascii=False)
            # 替换内容
            json_str = json_str.replace(search_string, replacement_string)
            # 将字符串转换回JSON格式
            json_obj = json.loads(json_str)
            self.fileContent = json_obj
            print('文字更换完成')
            self.generate_json()



    # 生成json文件，替换原来的json文件

    def generate_json(self):
        print('生成json文件开始')
        with open(self.targetFile, 'w', encoding='utf-8') as file:
            json.dump(self.fileContent, file, ensure_ascii=False, indent=4)
            print('生成json文件完成')