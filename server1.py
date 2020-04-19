import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
# s.bind(("192.168.1.96", 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established.")
	msg = bytes("Welcome to the server.", "utf-8")
	clientsocket.send(msg)