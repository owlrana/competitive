# to talk to a network web server (usually on port 80)
# this code does not send any data, just dials the phone

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.SOCK_STREAM = series of characters incoming outgoing
mysock.connect( ('data.pr4e.prg', 80) ) #data.pr4e.prg is the host (domain name), 80 is the port