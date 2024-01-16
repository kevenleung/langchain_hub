

from task.topic_task import handle_topic_classify
from task.chat_task import handle_chat_task
from task.task_demo import handle_demo_task


def handle_task(query, uid, task):
    res = {}
    # 此处转发业务处理
    if task == 'demo':
        res = handle_demo_task(query, uid)
    if task == 'topic':
        res = handle_topic_classify(query, uid)
    elif task == 'chat':
        res = handle_chat_task(query, uid)
    
    return res