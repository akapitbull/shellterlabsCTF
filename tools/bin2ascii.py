#!/usr/bin/env python
# chmod +x bin2ascii.py && mov bin2ascii.py bin2ascii && mv bin2ascii /usr/bin
import sys

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

if len(sys.argv) > 1:
    text = str(sys.argv[1]).replace(' ','')
    str_ = ""
    for code in chunkstring(text,8): 
        code = int(code, 2)
        char = chr(code)
        str_ += char
    	
    print(str_)
else:
    print('Usage : bin2ascii "binary_text"')
    
