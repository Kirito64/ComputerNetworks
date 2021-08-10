import socket 

from threading import *

clientSocket = socket.socket()

host = "localhost"
port = 12345
seprator_token = "<NEP>"
disconectMessage = "!DISCONNECT"
print("waiting for connection")
try:
	clientSocket.connect((host, port))
except socket.error as e:
	print(str(e))

print("[+] Connected.")

name = input("Enter your name")

def clientListener():
	while True:
		message = clientSocket.recv(1024).decode()
		print("\n", message)

t = Thread(target=clientListener, args=())
t.daemon = True

t.start()

print("To quit type q")

while True:
	data = input()
	if data.lower() == "q":
		break

	datasend = f"{name}{seprator_token}{data}"

	clientSocket.send(datasend.encode())

clientSocket.send(disconectMessage.encode())
clientSocket.close()