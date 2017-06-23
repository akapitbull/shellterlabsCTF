from __future__ import division
from decimal import Decimal
import sys
import time
import socket

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
received = ''

print '------------------------------'
received = s.recv(1024).strip()
print '[<] %s' % received
try:
	response = Decimal(eval(received))
except ZeroDivisionError:
	response = 0
s.send(str(response)+'\n')
print '[>] %s' % response
time.sleep(1)

while not 'shellter' in received:
    received = s.recv(1024).strip()
    l1 = received.split('\n')
    print '[r] %s' % l1[0]
    print '------------------------------'
    print '[<] %s' % l1[1]
    if str(l1[1]).find('shellter') != -1:
        break 
    try:
    	response = Decimal(eval(l1[1]))
    except ZeroDivisionError:
    	response = 0

    s.send(str(response)+'\n')
    print '[>] %s' % response
    time.sleep(1)
    