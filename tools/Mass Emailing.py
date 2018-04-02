#!-*- conding: utf8 -*-
#In order to use GMAIL accounts, you must enable permission in the gmail account settings in the LINK below
#https://myaccount.google.com/lesssecureapps?pli=1

from validate_email import validate_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
import time

# SET EMAIL BODY
message = '<h1>Ola amigo!</h1> <h4>Voce gosta de Seguranca da Informacao ?</h4> Pra voce que gosta da area de Seguranca da Informacao,recomendamos dar uma olhadinha nesse <strong>Novo Canal</strong> no <a href="https://www.youtube.com/playlist?list=PLlq-hlhs91wqtRtIgQRxmqvgqTDZn6Qhu"> youtube </a>. <h5>Descricao previa do canal :</h5> O canal pretende mostrar a resolucao de desafios no estilo Capture The Flag (CTF), proposto no portal shellterlabs.com, onde cada desafio envolve uma ou mais tecnicas que juntas compoem <strong>O mundo</strong> da Seguranca da Informacao. <br> <strong>Os desafios incluem categorias como:</strong> <ul> <li>Criptografia</li> <li>Steganografia</li> <li>Bruteforce</li> <li>Injecao SQL</li> <li>Exploracao Web</li> <li>Engenharia reversa</li> <li>Analise e Pericia Forense</li> <li>etc...</li> </ul> <h5>Links relacionados:</h5> Github: https://github.com/sql3t0 <br> Twitter: https://twitter.com/sqleto <br> Video da Playlist: https://youtu.be/GtIxocSsIdU?list=PLlq-hlhs91wqtRtIgQRxmqvgqTDZn6Qhu'

def sendMail(email,txt,c):
		# create message object instance
		msg = MIMEMultipart()
		
		#create server
		server = smtplib.SMTP('smtp.gmail.com: 587') # SMTP ADDRESS AND PORT FOR GMAIL USERS 
		server.ehlo()
		server.starttls()
		 
		# Login Credentials for sending the mail
		password = "SET_PASS" # SET USER PASSWD  
		msg['From'] = "source_mail@gmail.com" # SET SOURCE EMAIL   
		server.login('SET_HERE', password)# SET DESTINATION EMAIL  

		# setup the parameters of the message
		message = txt
		msg['Subject'] = "SUBJECT_HERE" # SET EMAIL SUBJECT
		msg['To'] = email

		# add in the message body
		msg.attach(MIMEText(message, 'html')) #SET EMAIL TYPE (plain or html) 
		
		# send the message via the server.
		server.sendmail(msg['From'], msg['To'], msg.as_string())
		sys.stderr.writelines("\r[+]["+str(c)+"]successfully sent email to %s " % (m.replace('\n',''))+"                         ")
		server.quit()

if(len(sys.argv) < 2):
	print 'Usage : '+sys.argv[0]+' "path/to/mailList.txt" '
else:
	count = 0
	for m in open(sys.argv[1]):
		if validate_email(m):
			try:
				sendMail(m,message,count)
				count= count + 1
			except smtplib.SMTPException:
				sys.stderr.writelines("\r[-]["+str(count)+"]Sequential send time overflow !")
				time.sleep(300) # SLEEP 5min
				sys.stderr.writelines("\r[>]Resuming...")
				sendMail(m,message,count)
				continue
		else:
			continue

	print "\n[+] Task Completed !"
		
