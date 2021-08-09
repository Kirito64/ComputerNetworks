import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



port = 12345



s.bind(('localhost', port))

s.listen(5)

while True:
	c, addr = s.accept()

	print("client connected from ", addr)
	c.send(str.encode("Thanks for connected"))

s.close()