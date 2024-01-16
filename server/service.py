
import json
from flask import Flask, request
from task.task import handle_task
from server.account.token import verify_token
from configs.server_info import tasks
from configs.server_info import ServerConfig


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def root():
    return "Welcome to chatglm model."

@app.route("/robot",methods=["POST"])
def robot():
    data_seq = request.get_data()
    data_dict = json.loads(data_seq)
    # 验证token是否仍然有效或者合法
    uid = verify_token(data_dict.get('token', None))
    if uid is None:
        # TODO 记录用户访问异常日志
        return {'code': 401, 'msg': '无效用户'}
    # else:
        # TODO 可以开启该用户的操作日志记录
    
    query = data_dict.get("human_input", '')
    # 识别任务
    task = data_dict.get('task', None)
    if task not in tasks:
        task = tasks[0]
    data = handle_task(query=query, uid=uid, task=task)
    if data is None:
        res = {'data': '', 'code': 600, 'msg': '系统异常 600'}
    else:
        res = {'data': data, 'code': 200, 'msg': 'ok'}

    res = json.dumps(res, ensure_ascii=False)
    return res


def start_server():
    server = ServerConfig()
    app.run(host=server.host, port=server.port, debug=False)
    





