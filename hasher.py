#!/usr/bin/python

import hashlib

hashvalue = input("* Enter a string to hash: ")

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print(hashobj1.hexdigest())

