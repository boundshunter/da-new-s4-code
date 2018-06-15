#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
#!/usr/bin/env python3.6
import socket,os,hashlib
server = socket.socket()
server.bind(('127.0.0.1',9998))
server.listen(5)

while True:
    print("Wait for connect...")
    conn, addr = server.accept()
    while True:
        print("Connect incoming.")
        data = conn.recv(1024)
        if not data:
            print("Client has disconnect")
            break
        cmd, filename = data.decode().split()
        if os.path.isfile(filename):
            f = open(filename,'rb')
            m = hashlib.md5()
            # 获取文件大小
            file_total_size = os.stat(filename).st_size
            conn.send(str(file_total_size).encode()) # 发送文件大小
            conn.recv(1024) # 等待 ack
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5:",m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode()) # 发送md5值
server.close()