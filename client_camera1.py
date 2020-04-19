import socket
import pickle
import numpy as np
import cv2
import sys
import errno

import socket_functions1 as sf


HEADER_LENGTH = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
# s.setblocking(False)

while True:
    try:
        # message = sf.receive_message(s, HEADER_LENGTH)
        message = sf.receive_pickle_message(s, HEADER_LENGTH)
        if message != False:
            print(message["header"])

            frame = message["data"]

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        if message == False:
            sys.exit()


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