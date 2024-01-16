# 关闭server和client
ps -eo pid,user,cmd|grep -P 'server/start_server.py|client/start_chat.py|multiprocessing'|grep -v grep|awk '{print $1}'|xargs kill -9