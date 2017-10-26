#!/usr/bin/env python

import sys

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def cipher(ciphertext):
	plaintext = ""
	for i in range(26):
		for c in ciphertext.upper():
		    if c.isalpha(): 
		    	plaintext += I2L[ (L2I[c] - i)%26 ]
		    else: 
		    	plaintext += c
		plaintext = plaintext + "\n"     	
	
	return plaintext
	   	
if len(sys.argv) <= 1 :
	print('Usage : caesarCipher.py "string_sequency"')
else:
	print cipher(sys.argv[1])