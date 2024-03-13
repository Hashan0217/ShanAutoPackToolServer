import os


import git

class autoMatedGitWorkFlow:
    def __init__(self, filePath):
        self.repo = None
        self.path = filePath


    # 初始化git
    def gitInit(self):
        # 构建 .git 文件夹路径
        git_dir = os.path.join(self.path, '.git')

        # 检查 .git 文件夹是否存在
        if os.path.exists(git_dir) and os.path.isdir(git_dir):
            print('Git 存在 直接使用')
            self.repo = git.Repo(self.path)

        else:
            print('Git 不存在 初始化中...')
            self.repo = git.Repo.init(self.path)
            self.add()
            self.commit('Initial commit')
            print('Git 初始化完毕')

    # 添加分支
    def addBranch(self, branchName):
        self.repo.create_head(branchName)
        print('Branch created')

    # 切换分支
    def checkoutBranch(self, branchName):
        self.repo.git.checkout(branchName)
        print('Branch switched')

    # 查看状态
    def status(self):
        print(self.repo.git.status())
        return self.repo.is_dirty()


    # add
    def add(self):
        self.repo.git.add('.')
        print('Add completed')

    def commit(self, commitMessage):

        # 转换字符串
        self.repo.git.commit(m=commitMessage)
        print('Commit completed')

        # self.repo.git.commit(m=commitMessage)
        # print('Commit completed')
    def autoCommit(self, commitMessage):
        isOk = self.status()
        if not isOk:
            print('状态为空，不需要提交')
            return
        self.add()
        self.commit(commitMessage)
        print('Auto commit completed')

