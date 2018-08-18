import sys

#ErorainZWI[kYehVcT
msg=sys.argv[1]

r=''
for i in range(len(msg)):
	r+= chr(ord(msg[i])+i)
print '  : '+r

r=''
for i in range(len(msg)):
	r+= chr(ord(msg[i])-i)
print '  : '+r

#GuswgpvcaTgxgtxgug
for i in range(255):
	r=''
	for x in sys.argv[1]:
		try:
			r += chr(ord(x)+i)
		except Exception as e:
			r += chr(ord(x)+i - 255)
			
	print str(i)+' : '+r

	r=''
	for x in sys.argv[1]:
		try:
			r += chr(ord(x)-i)
		except Exception as e:
			r += chr(ord(x)-i + 255)
			
	print str(i)+' : '+r