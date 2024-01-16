# -*- coding: utf-8 -*-

# 用户模型
def singleton_user(cls):
    instances = {}
    def _singleton(param=None, *args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(param, *args, **kwargs)
        return instances[cls]
 
    return _singleton