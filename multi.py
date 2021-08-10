import socket
import os
from threading import *


Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 12345

seprator_token = "<NEP>"
disconectMessage ="!DISCONNECT"
threadCount = 0
clientSockets = set()

Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
	Server.bind((host, port))

except socket.error as e:
	print(str(e))

print("Server Listening on port " + str(port))

Server.listen(5)

def ServerListner(cs):
	while True:
		try:
			msg = cs.recv(1024).decode()
		except Exception as e:
			print(f"[1] Error: {e}")
			cs.close()
			break
			# clientSockets.remove(cs)
		else:
			if msg == disconectMessage:
				cs.close()
				break

			msg = msg.replace(seprator_token, ": ")
		for client_socket in clientSockets:
			try:
				client_socket.send(msg.encode())
			except socket.error as e:
				client_socket.close()

				clientSockets.remove(client_socket)
	
	clientSockets.remove(cs)


while True:
	cs, caddr = Server.accept()
	print(f"[+] {caddr} connected to server.")
	
	clientSockets.add(cs)
	print(f"Total active connections: {len(clientSockets)}")
	welcome = f"Thanks for Connecting to the server {caddr}"
	cs.send(welcome.encode())
	t = Thread(target=ServerListner, args=(cs,))
	t.daemon = True
	t.start()


for cs in clientSockets:
	cs.close()

Server.close()


