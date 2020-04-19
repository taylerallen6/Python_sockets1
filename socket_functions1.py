import socket
import time
import pickle
import numpy as np
import cv2


# Handles message receiving
def receive_message(client_socket, HEADER_LENGTH):
	try:
		# Receive our "header" containing message length, it's size is defined and constant
		message_header = client_socket.recv(HEADER_LENGTH)

		# If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
		if not len(message_header):
			return False

		# Convert header to int value
		message_length = int(message_header.decode('utf-8').strip())

		# Return an object of message header and message data
		data = client_socket.recv(message_length).decode("utf-8")
		return {'header': message_header, 'data': data}

	except:
		# If we are here, client closed connection violently, for example by pressing ctrl+c on his script
		# or just lost his connection
		# socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write)
		# and that's also a cause when we receive an empty message
		return False


def send_message(client_socket, HEADER_LENGTH, message):

	# Encode message to bytes, prepare header and convert to bytes, like for username above, then send
	message = message.encode('utf-8')
	message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
	message = message_header + message

	client_socket.send(message)


def receive_pickle_message(client_socket, HEADER_LENGTH):
	try:
		# Receive our "header" containing message length, it's size is defined and constant
		message_header = client_socket.recv(HEADER_LENGTH)

		# If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
		if not len(message_header):
			return False

		# Convert header to int value
		message_length = int(message_header.decode('utf-8').strip())
		print(message_length)

		# Return an object of message header and message data
		data = client_socket.recv(message_length)
		print(len(data))
		data = pickle.loads(data)
		return {'header': message_header, 'data': data}


	except:
		# If we are here, client closed connection violently, for example by pressing ctrl+c on his script
		# or just lost his connection
		# socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write)
		# and that's also a cause when we receive an empty message
		return False


def receive_pickle_message(client_socket, HEADER_LENGTH):
	try:
		# Receive our "header" containing message length, it's size is defined and constant
		message_header = client_socket.recv(HEADER_LENGTH)

		# If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
		if not len(message_header):
			return False

		# Convert header to int value
		message_length = int(message_header.decode('utf-8').strip())
		print(message_length)

		data = b''
		while len(data) != message_length:
			# Return an object of message header and message data
			data += client_socket.recv(message_length)
			print(len(data))

		data = pickle.loads(data)
		return {'header': message_header, 'data': data}


		# full_msg = b''
	 #    new_msg = True
	 #    while True:
	 #        msg = s.recv(16)
	 #        if new_msg:
	 #            print("new msg len:",msg[:HEADERSIZE])
	 #            msglen = int(msg[:HEADERSIZE])
	 #            new_msg = False

	 #        print(f"full message length: {msglen}")

	 #        full_msg += msg

	 #        print(len(full_msg))

	 #        if len(full_msg)-HEADERSIZE == msglen:
	 #            print("full msg recvd")
	 #            print(full_msg[HEADERSIZE:])
	 #            print(pickle.loads(full_msg[HEADERSIZE:]))
	 #            new_msg = True
	 #            full_msg = b""

	except:
		# If we are here, client closed connection violently, for example by pressing ctrl+c on his script
		# or just lost his connection
		# socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write)
		# and that's also a cause when we receive an empty message
		return False


def send_pickle_message(client_socket, HEADER_LENGTH, message):

	# Encode message to bytes, prepare header and convert to bytes, like for username above, then send
	message = pickle.dumps(message)
	message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
	message = message_header + message

	client_socket.send(message)
	