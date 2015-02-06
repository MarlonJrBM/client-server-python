#!/usr/bin/python

##client.py
from socket import *
import sys

WELCOME_MESSAGE = 'Welcome to this simple browser! Type the url or path you would like to visit and press enter. Type /quit if you want to exit the application'

INPUT_ERR_MESSAGE = 'Incorrect call. Please provide server address as input to the program in the command line.\nExample: ./client.py 192.168.75.2'

BROWSER_HEADER = '\n' + 50*'-' + '\n'

BROWSER_FOOTER = '\n' + 50*'-' + '\n'

if (len(sys.argv)<2):
	print INPUT_ERR_MESSAGE
	sys.exit()

HOST = sys.argv[1] #first argument passed to program
PORT = 80    #our port from before
ADDR = (HOST,PORT)
BUFSIZE = 4096


def formRequest(path):
	return "GET /{} HTTP/1.1".format(path)  

def main():

	print WELCOME_MESSAGE
	path = raw_input()
	
	while (path != '/quit'):
		response, buff = '',''
		cli = socket( AF_INET,SOCK_STREAM)
		cli.connect((ADDR))
		request = path
		cli.sendall(formRequest(path)) #sends request
		while 1:
			buff = cli.recv(BUFSIZE) #gets first chunk of message
			if not buff: break #if current chunk is empty, this is it
			response = response + buff #appends it to response
		print BROWSER_HEADER + response + BROWSER_FOOTER
		cli.close()
		path = raw_input()



main()




