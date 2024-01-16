from utils.singleton import singleton_user

# 用户信息 !!!当前客户端暂不支持登录获取token功能,如需要token, 请联系服务端人员
@singleton_user
class User(object):
    def __init__(self, uid):
        super().__init__()
        self.uid = uid
        self.token = 'abcxxx'   # 如果是远程连接,可以使用持久化存储和读取
        self.name = ''
