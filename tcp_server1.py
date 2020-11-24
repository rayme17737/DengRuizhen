"""
tcp套接字服务端
"""

from socket import *
import time

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(('0.0.0.0', 8888))

tcp_socket.listen(5)

while True:
    print("watting for connect...")
    connfd, addr = tcp_socket.accept()
    print("connect from:", addr)

    while True:
        data = connfd.recv(5)
        # if data == b"##":
        # if not data:
        #     print("服务器退出")
        #     break
        print("receive:", data.decode())
        # 粘包问题解决方法
        connfd.send(b"thanks#")  # 设置边界
        # time.sleep(0.1)  # 控制消息发送速度

    connfd.close()

tcp_socket.close()
