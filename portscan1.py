#!/usr/bin/python

import socket
from termcolor import colored
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = "localhost"
#host = raw_input("[*] Enter The Host to Scan:")

#port = 80

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(colored("Port %d is closed, im looking for next" % (port), 'red'))
		#i=i+1 
	else:
		print(colored("Port %d is opened" % (port), 'green'))

for port in range(1,1000):
	portscanner(port)
 

