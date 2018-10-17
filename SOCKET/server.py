import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('连接地址：')
    print(addr)
    c.send('hello cwt!'.encode(encoding='utf-8',errors='strict'))
    c.close()
