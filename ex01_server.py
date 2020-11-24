"""
tcp套接字服务端
"""

from socket import *
import time


def recv_image(connfd):
    filename = "%d-%d-%d.jpg" % time.localtime()[:3]
    fw = open(filename, "wb")
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        fw.write(data)
    # connfd.send("上传完成".encode())


def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(('0.0.0.0', 8888))
    tcp_socket.listen(5)

    while True:
        print("watting for connect...")
        connfd, addr = tcp_socket.accept()
        print("connect from:", addr)
        recv_image(connfd)
        # print("receive:", data.decode())
        connfd.close()
    tcp_socket.close()


if __name__ == '__main__':
    main()
