import os
from utils.file_utils import read_configer
import langchain
from langchain.cache import InMemoryCache
import logging


# 开启日志
logging.basicConfig(level=logging.INFO)

# 启动llm的缓存
langchain.llm_cache = InMemoryCache()

# 当前支持的任务, 默认任务为chat
tasks = ['chat', 'topic', 'demo']

# 服务器端
server_config_path = f"{os.path.abspath('.')}/server/configs/server_config.yaml"

class ServerConfig:
    def __init__(self):
        super().__init__()
        self.host = None
        self.port = None
        self._load_config(server_config_path)

    def _load_config(self, path):
        server_conf = read_configer(path)
        self.host = server_conf['server_host']
        self.port = server_conf['server_port']


# 大模型: 
llms_conf_path = f"{os.path.abspath('.')}/server/configs/server_config.yaml"

# 只需要与model端保存一致就行
class LLMsConfig:
    def __init__(self, conf_type):
        super().__init__()
        self.llms = self._load_config(conf_type)

    def _load_config(self, key):
        info = read_configer(llms_conf_path)
        datas = {}
        if key == 'llms':
            datas = info.get(key, {})
        
        return datas
