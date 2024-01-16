import psutil

# 判断本地端口是否被占用
def is_port_in_use(port:int):
    for proc in psutil.process_iter():
        for con in proc.connections():
            if con.status == 'LISTEN' and con.laddr.port == port:
                return True
    return False


# 查看端口使用情况
def check_ports(ports):
    res = {}
    for port in ports:
        if is_port_in_use(port):
            res['port'] = 'opened'
        else:
            res['port'] = 'closed'
    return res


# 判断是否为端口（1-5位)
def is_valid_port(port): 
    try:  
        port = int(port)  
        if 1 <= port <= 65535:  
            return True  
        else:  
            return False  
    except ValueError:  
        return False