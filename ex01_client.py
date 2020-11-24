"""
tcp套接字客户端
"""

from socket import *

ADDR = ("127.0.0.1", 8888)
filename = "timg.jfif"
def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(ADDR)
    fr = open(filename, "rb")
    while True:
        data = fr.read(1024)
        if not data:
            break
        tcp_socket.send(data)
    data = tcp_socket.recv(1024)
    print("from server:", data.decode())
    tcp_socket.close()


if __name__ == '__main__':
    main()