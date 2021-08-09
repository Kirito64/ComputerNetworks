import socket
import os
from _thread import *

def threadedClient(connection):
	connection.send(str.encode("Welcome to the Server"))

	while True:
		data = connection.recv(2048)
		reply = "server says" + data.decode("utf-8")
	
		if not data:
			break;
		connection.sendall(str.encode(reply))
	connection.close()



Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 12345

threadCount = 0

try:
	Server.bind((host, port))

except socket.error as e:
	print(str(e))

print("Server Listening on port " + str(port))

Server.listen(5)


while True:
	c,addr = Server.accept()
	print("Connection to" + str(addr[0]) + "From" + str(addr[1]))

	start_new_thread(threadedClient, (c,))
	threadCount += 1

	print("Thread Count: " + str(threadCount))

Server.close()


