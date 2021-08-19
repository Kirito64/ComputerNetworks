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
nameaccess={}

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
			print(f"Error: {e}")
			cs.close()
			break
			# clientSockets.remove(cs)
		else:
			if msg == disconectMessage:
				cs.close()
				break

			msg = msg.replace(seprator_token, ": ")
			print(msg)
			counter=0
			finname=''
			while msg[counter]!=':':
				finname+=msg[counter]
				counter+=1
			counter+=2
			namestr=''
			while msg[counter]!=' ':
			    namestr+=msg[counter]
			    counter+=1
			names=[]
			temp=''
			print(namestr)
			msg2=''
			while counter<len(msg):
				msg2+=msg[counter]
				counter+=1
			for letter in namestr:
			    if letter!='_':
			        temp+=letter
			    else:
			        if temp=='all':
			            names=clientSockets
			            break
			        names.append(nameaccess[temp])
			        temp=''
		msg=finname+': '+msg2
		for client_socket in names:
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
	usname = cs.recv(1024).decode()
	print(usname)
	nameaccess[usname]=cs
	t = Thread(target=ServerListner, args=(cs,))
	t.daemon = True
	t.start()


for cs in clientSockets:
	cs.close()

Server.close()