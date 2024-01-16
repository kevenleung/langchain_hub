import logging
import time
from llm.llm_chat import Chat

def init_chat_cli(host, port, task=''):
    llm = Chat() # 创建聊天模型对象
    while True:
        human_input = input("Human: ")
        begin_time = time.time() * 1000
        # 当前支持的任务为['chat', 'topic', demo], 默认为chat
        response = llm(human_input, stop=["you"], task=task, host=host, port=port, route='/robot')
        end_time = time.time() * 1000
        used_time = round(end_time - begin_time, 3)
        logging.info(f"process time: {used_time}ms")
        print(f"{response}")



    
    

