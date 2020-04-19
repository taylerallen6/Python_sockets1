import socket
import time
import pickle
import numpy as np
import cv2
import errno
import sys
from socket import error as SocketError

import socket_functions1 as sf


HEADER_LENGTH = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

cap = cv2.VideoCapture(0)

while True:
	# now our endpoint knows about the OTHER endpoint.
	client_socket, address = s.accept()
	print(f"Connection from {address} has been established.")

	while True:
		try:
			# time.sleep(2)
			# Capture frame-by-frame
			ret, frame = cap.read()
			# print(frame.shape)

			# Wait for user to input a message
			# message = input('enter message > ')
			# message = "hello"
			# sf.send_message(client_socket, HEADER_LENGTH, message)

			# frame = [1,2,3]

			sf.send_pickle_message(client_socket, HEADER_LENGTH, frame)

		except IOError as e:
			# This is normal on non blocking connections - when there are no incoming data error is going to be raised
			# Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
			# We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
			# If we got different error code - something happened
			if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
				print('Reading error: {}'.format(str(e)))
				sys.exit()

			# We just did not receive anything
			continue

		# except SocketError as e:
		#     if e.errno != errno.ECONNRESET:
		#         raise # Not error we are looking for
		#     pass # Handle error here.