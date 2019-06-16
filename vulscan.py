#!/usr/bin/python

import socket
import os
import sys

def retBanner(ip,port):
	print 'Banner'
	try:
		socket-setdefaulttimeout(2)
		s = socket.socket()
		print 'Test to connect '
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner, filename):
	print 'Czeck'
	f = open(filename, "r")
	for line in f.readlines():
		if line.strip("\n") in banner:
 			print '[+] Server is vulnerable: '+banner.strip("\n")
		else:
			print 'Host is good'

def main():
	if len(sys.argv) == 2:
		filename=sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] File Doesnt Exist !'
			exit(0)
		if not os.access(filename, os.R_OK):
			print '[-] Access Denied !'
			exit(0)
	else:
		print '[-] Usage: ' + str(sys.argv[0]) + " <vuln filename>"
		exit(0)
	portlist = [21,22,25,80,110,443,445]
	#for x in range(0,10):
	#ip="172.20.10." + str(x)
	ip="localhost"
	for port in portlist:
		banner = retBanner(ip,port)
		if banner:
			print '[+] ' + ip + "/" + str(port) + " : " +banner
			checkVulns(banner, filename)

main()


