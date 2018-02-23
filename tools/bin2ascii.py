#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    text = str(sys.argv[1]) #raw_input("Please enter binary data: ")
    chars = text.split()
    str_ = ""
    for code in chars:
    	code = int(code, 2)
    	char = chr(code)
    	str_ += char
    
    print(str_)
else:
    #chars = sys.argv[1:]
    print('Usage : bin2ascii "binary_text"')
    
