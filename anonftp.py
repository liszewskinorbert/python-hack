#!/usr/bin/python


import ftplib

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymus', 'anonymus')
		print "[*] " + hostname + " FTP Anonymus Logon Succeeded."
		ftp.quit()
		return True
	except Exception, e:
		print "[-] " + hostname + " FTP Anonymus Logon Failed."

host = raw_input("Enter the Ip Address : ")
anonLogin(host)


