#!/usr/bin/python
#server.py
from socket import *      #import the socket library
from server_functions import *

##let's set up some constants
HOST = ''    #we are the host
PORT = 80    #arbitrary port not currently in use
ADDR = (HOST,PORT)    #we need a tuple for the address
BUFSIZE = 4096    #reasonably sized buffer for data
serv = socket(AF_INET, SOCK_STREAM)

def main():
	## now we create a new socket object (serv)
	## see the python docs for more information on the socket types/flags

	##bind our socket to the address
	serv.bind((ADDR))    #the double parens are to create a tuple with one element
	serv.listen(5)    #5 is the maximum number of queued connections we'll allow
	print 'Listening on port ' + str(PORT)

	while 1:

		conn,addr = serv.accept() #accept the connection
		print 'Conencted by ', addr
		request = conn.recv(BUFSIZE) #gets request
		print 'Received Request ', request
		conn.sendall(parseRequest(request)) #sends response
		print 'sent response'
		conn.close()
		print 'closed connection'

	

try:
	main()
finally:
	serv.close()


