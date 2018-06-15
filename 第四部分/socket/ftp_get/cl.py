#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
#!/usr/bin/env python3.6
import socket,os,hashlib
client = socket.socket()
client.connect(('127.0.0.1',9998))

while True:
    cmd = input(">>:").strip()
    if not cmd:continue # cmd 为空，返回循环继续重新开始

    if cmd.startswith("get"):
        client.send(cmd.encode())
        sv_response = client.recv(1024).decode() # 接收大小
        print("sv_response:",sv_response)

        client.send("ack ok".encode())

        file_total_size = int(sv_response)
        print(type(file_total_size),file_total_size)
        filename = cmd.split()[1]
        m = hashlib.md5()
        f = open(filename + '.bak','wb')
        received_size = 0
        while received_size < file_total_size:
            if file_total_size - received_size > 1024:
                size = 1024
            else:
                size = file_total_size - received_size
                print("last recv size",size)
            data = client.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            client_file_md5 = m.hexdigest()
            print("client_file_md5_value:",client_file_md5)
            f.close()
        sv_file_md5 = client.recv(1024).decode()
        print("server_file_md5_value:",sv_file_md5)
client.close()