from models.chatglm3.chatglm3 import ChatGLM3
from models.embedding import Embbeding
from utils.network_utils import is_port_in_use
from configs.model_info import LLMsConfig
from models.chatglm3.chatglm3_service import start_model_server as start_chatglm3

# 启动大模型
def init_model():
    # llms
    for llm in LLMsConfig(conf_type='llms').llms:
        host = llm['host']
        port = llm['port']
        if not is_port_in_use(port=port):
            print(f"正则加载大模型 [{llm['name']}] 请稍等...")
            try:
                if llm['name'] == 'chatglm3-6b':
                    ChatGLM3(path=llm['path'])
                    # Embbeding()     # 如果需要使用到向量库，需要开启，否则请注释
                    res = start_chatglm3(host=host, port=port)
                    if not res:
                        print(f"{llm['host']}:{llm['port']}服务开启失败!")
                else:
                    print(f"暂不支持 [{llm_info['name']}]")
            except Exception as e:
                print(f'[{llm["name"]}] 加载失败!!!')
            finally:
                continue
            
        else:
            print(f"[{llm['name']}]已加载, {llm['host']}:{llm['port']}服务已开启, 注: 如有问题, nvidia-smi查看显存情况, ps x 查看进程")
    
    # embeddings
    embeddings_info = LLMsConfig(conf_type='embeddings')



if __name__ == "__main__":
    init_model()
