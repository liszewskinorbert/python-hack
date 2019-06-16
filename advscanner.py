#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored
def connScan(tgtHost, tgtPort):
	try:
		sock=socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost, tgtPort))
		print(colored('[+] %d/tcp Open' % tgtPort, 'green'))
	except:
		print(colored('[-] %d/tcp Closed' % tgtPort, 'red'))
	finally:
		sock.close()


def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print 'Unknown Host %s ' %tgtHost
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '[+] Scan results for:' + tgtName[0]
	except:
		print '[+] Scan results for:' + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t=Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()


def main():
	parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port> or <target port, target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specyfy targeet host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specyfi target ports separated by coma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	main()

