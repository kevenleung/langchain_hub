nohup python server/start_server.py >> ./server/log/service_log.txt 2>&1 &
sleep 1s

python client/start_chat.py