"""
tcp套接字客户端
"""

from socket import *
import re

ADDR = ("127.0.0.1", 8888)

while True:
    data = input("我:")
    if not data:
        break
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(ADDR)
    tcp_socket.send(data.encode())
    data = tcp_socket.recv(1024)
    print("from 小美:", data.decode())

tcp_socket.close()
