#!/usr/bin/python
#By Sql3t0
from pwn import *

sr = remote('158.69.192.239', 1337)
print r.recv(2048)
r.send("start")
print r.recv()

while True:	
	rec = r.recv()
	if "EY{" in rec:
		print rec
		break
	
	print rec
	m = 0	
	for n in eval(rec):
		if n > m:
			m = n	
	
	print '[+]Resposta : '+str(m)	
	r.send(str(m))
