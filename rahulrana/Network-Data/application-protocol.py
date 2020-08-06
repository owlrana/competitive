# HTTP - Hypertext Transfer Protocol started as a basic protocol and has evolved into one of the best now
# URLs - Uniform Resource Locator contains protocol, host and then the document

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#if the code works till now, means that the derver you're accsing does have a backend and it is connected.
#now according to HTTP protocol, server does a RECIEVE first and we do a SEND first, so we send data

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() 
mysock.send(cmd)

while True:
    data = mysock.recv(512) #we recieve upto 512 characters
    if (len(data) < 1): #if we do not recieve the data, it means it's the end of file (or trasnmition)
        break
    print(data.decode()) #now we decode it
mysock.close() #always close it otherwise it will eat up resources