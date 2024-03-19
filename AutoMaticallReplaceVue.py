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



