

# 验证用户是否有效
def verify_token(token):
    uid = None
    
    # TODO 匹配数据库中的用户信息
    # +++++++++++++++++++
    if token is not None:
        uid = 'kele123'
    # +++++++++++++++++++
    
    return uid