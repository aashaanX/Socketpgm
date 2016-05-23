#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("localhost",12346))

sock.listen(2)

while True:
	conn,addr = sock.accept() 
	data = conn.recv(1024).decode("ascii")
	print("Data recived from client is :",data)
	print("the same data will be returned back to client")
	conn.send(data.encode())
	conn.close()

