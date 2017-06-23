#!/usr/bin/env python
# coding=utf-8
FILE_IN = 'flag.enc'
FILE_OUT = 'flag.dec'

def decrypt():
    data = [ord(c) for c in open(FILE_IN, 'rb').read()]

    # We know data[len(data) - 1] is already plaintext (as it was not encrypted)
    for i in reversed(xrange(len(data) - 1)):
        data[i] = data[i] ^ data[i + 1]

    decrypted = ''.join([chr(b) for b in data])

    f = open(FILE_OUT, 'wb')
    f.write(decrypted)
    f.close()

decrypt()