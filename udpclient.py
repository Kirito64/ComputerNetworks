import socket
import threading
import random
import os
from colorama import Fore, init



init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
] 

def ReceiveData(sock):
    while True:
        try:
            data,addr = sock.recvfrom(1024)
            print(data.decode('utf-8'))
        except:
            pass

def RunClient(serverIP):
	clientColor = random.choice(colors)
	host = socket.gethostbyname(socket.gethostname())
	port = random.randint(6000,10000)
	print('Client IP->'+str(host)+' Port->'+str(port))
	server = (str(serverIP),5000)
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host,port))

	name = input('Please write your name here: ')
	if name == '':
		name = 'Guest'+str(random.randint(1000,9999))
		print('Your name is:'+name)
	s.sendto(name.encode('utf-8'),server)
	threading.Thread(target=ReceiveData,args=(s,)).start()
	while True:
		data = input()
		if data == 'qqq':
			break
		elif data=='':
			continue
		data = f"{clientColor}[{name}]->{data}{Fore.RESET}"
		s.sendto(data.encode('utf-8'),server)
	s.sendto(data.encode('utf-8'),server)
	s.close()
	os._exit(1)


RunClient("192.168.56.1")
