class VueFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path


    def read_vue_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"文件 '{self.file_path}' 未找到")
            return None

    def write_vue_file(self, content):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"成功写入文件 '{self.file_path}'")
        except Exception as e:
            print(f"写入文件 '{self.file_path}' 时出现错误: {e}")

    def modify_vue_file(self, search_string, replacement_string):
        content = self.read_vue_file()
        if content is not None:
            modified_content = content.replace(search_string, replacement_string)
            self.write_vue_file(modified_content)


# 创建 VueFileHandler 实例
vue_file_path = 'E:/temppp/tempCarrr/App.Vue'
vue_handler = VueFileHandler(vue_file_path)

# 读取 Vue 文件
vue_content = vue_handler.read_vue_file()
if vue_content is not None:
    print("Vue 文件内容:")
    print(vue_content)

# 修改 Vue 文件
search_string = 'huawei'
replacement_string = 'oppo'
vue_handler.modify_vue_file(search_string, replacement_string)
