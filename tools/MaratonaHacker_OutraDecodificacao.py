import sys
'''
txt = 6d486163107101114123052083067073073063115104111106063122063116543353066064083051083125
[m]
[H](0)
[a](=){1}
[c](?){3}
(k){G}
(e){A}
(r){L}
({){S}
(4){*}
(S)
(C){7}
(I){;}
(I){;}
(?){3}
(s){M}
(h){D}
(o){I}
(j){F}
(?){3}
(z){R}
(?){3}
(t){N}
[T](6){,}
[3](!)
[S](5){+}
(B){6}
(@){4}
(S)
(3){)}
(S)
(}){U}
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
		

