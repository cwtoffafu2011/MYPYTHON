#_*_coding:utf-8_*_
#!/usr/bin/env python


import socket

# 多线程并发的socket客户端
# SOCK_STREAM : tcp 长连接
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8080))

while True:
    msg=input('>>: ').strip()
    if not msg:continue

    s.send(msg.encode('utf-8'))
    data=s.recv(1024)
    print(data)
