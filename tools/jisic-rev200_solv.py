from subprocess import Popen, PIPE

for i in range(999):
	p = Popen("./r02", stdin = PIPE,stdout = PIPE)
	p.stdin.write('205'+"\r\n")
	p.stdin.write('543'+"\r\n")
	p.stdin.write(str(i)+"\r\n")
	print "["+str(i)+"]"
	print p.stdout.read()

	
