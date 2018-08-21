import sys
'''
txt = 6d486163107101114123052083067073073063115104111106063122063116543353066064083051083125
6d 48 61 63 = mHac
107 101 114 123 = ker{
052 083 067 073 073 = 4SCII
063 = 3 - c - ?
115 = s - M
104 = h - D
111 = o - I
106 = j - F
063 = ? - c - 3
122 = z - R
063 = ? - c - 3
116 = t - N
54  = 6 - T - ,
33  = ! - 3 - ESC
53  = 5 - S - +
066 = B - f - 6
064 = @ - d - 4
083 = S - 
051 = 3 - Q - )
083 = S 
125 = }
'''
txt = ['6d','48','61','63','107','101','114','123','052','083','067','073','073','063','115','104','111','106','063','122','063','116','54','33','53','066','064','083','051','083','125']
for l in txt:
	dec = ''

	try:
		dec += '[%s]'%l.decode('HEX')
	except Exception as e:
		#print e
		sys.stdout.write('\r')
	
	try:
		dec += '(%s)'%chr(int(l))
	except Exception as e:
		#print e
		sys.stdout.write('\r')

	try:
		if int(l,8) >= 32:
			dec += '{%s}'%chr(int(l,8))
	except Exception as e:
		#print e
		sys.stdout.write('\r')

	print dec
		

