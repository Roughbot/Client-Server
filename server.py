#!/usr/bin/python3
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000
serversocket.bind((host,port))
serversocket.listen(6)
while True:
	clientsocket,address = serversocket.accept()
	print("recived connection from" % str(address))
	message = "Hello there " + "\n\n"
	clientsocket.send(message)
	clientsocket.close()

