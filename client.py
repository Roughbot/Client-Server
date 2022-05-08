#!/usr/bin/python3
import socket
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = "host"
host = socket.gethostname()
port = 8000
clientsocket.connect(('host', 8000))
message = clientsocket.recv(1023)
clientsocket.close()
print(message)