
from chat_cli import init_chat_cli


if __name__ == "__main__":
    try:
        init_chat_cli(host='127.0.0.1', port=9203, task='demo')
    except Exception as e:
        print(f"3.客户端出现异常: {e}")
    