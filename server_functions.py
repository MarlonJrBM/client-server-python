#Auxiliary functions for server application
import os.path


ROOT_PATH = "/tmp/"
DEFAULT_OPEN_MODE = 'r'
SUCCESS_HEADER = "HTTP/1.1 200 OK\n"
FILE_NOT_FOUND_HEADER = 'HTTP/1.0 404 Not Found\n'
FILE_NOT_FOUND_PATH = '404.html'


def parseRequest(request):
	requestArray = request.split()
	if (requestArray[0]=='GET'):
		return fetchFile(requestArray[1].lstrip('/'))


def fetchFile(path):
	
	
	if (os.path.exists(ROOT_PATH + path)):
		with open(ROOT_PATH + path, DEFAULT_OPEN_MODE) as f:
			return SUCCESS_HEADER + f.read()
	else:
		return fileNotFound()



def fileNotFound():
	with open(FILE_NOT_FOUND_PATH, DEFAULT_OPEN_MODE) as f:
		return FILE_NOT_FOUND_HEADER + f.read()
	
