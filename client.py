#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("localhost",12346))
sock.send(input("what to send:").encode())

data = sock.recv(1024).decode("ascii")
print("data from server:",data)
sock.close()

