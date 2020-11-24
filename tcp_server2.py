"""
tcp套接字服务端
"""

from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(('0.0.0.0', 8888))

tcp_socket.listen(5)

while True:
    print("watting for connect...")
    connfd, addr = tcp_socket.accept()
    print("connect from:", addr)

    data = connfd.recv(1024)
    print("receive:", data.decode())
    connfd.send(b"thanks")
    connfd.close()

tcp_socket.close()
