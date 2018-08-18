#vguvauetkrv
import sys

def ascii_pp(msg):
	r=''
	for i in range(len(msg)):
		r+= chr(ord(msg[i])+i)
	print r

	r=''
	for i in range(len(msg)):
		r+= chr(ord(msg[i])-i)
	print r

	for i in range(255):
		r=''
		for x in msg:
			try:
				r += chr(ord(x)+i)
			except Exception as e:
				r += chr(ord(x)+i - 255)
				
		print r

		r=''
		for x in msg:
			try:
				r += chr(ord(x)-i)
			except Exception as e:
				r += chr(ord(x)-i + 255)
				
		print r

if len(sys.argv) <= 1 :
	if not sys.stdin.isatty():
		data = sys.stdin.read()
		print ascii_pp(data.replace('\n',''))
	else:
		print('Usage : scriptname.py "string_sequency"')
		print('      : or ')
		print('      : STDOUT | scriptname.py ')
else:
	if not sys.stdin.isatty():
		data = sys.stdin.read()
	else:
		data = sys.argv[1]
	
	print ascii_pp(data.replace('\n',''))
