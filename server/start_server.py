from service import start_server

if __name__ == "__main__":
    try:
        start_server()
    except Exception as e:
        print(f"1.服务发生异常: {e}")
    
    
    