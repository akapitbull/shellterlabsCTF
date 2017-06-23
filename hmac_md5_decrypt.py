from hashlib import sha1
import hmac
import itertools
import sys

target_hash = "aba70621e382c57e0b0173642eb6479c"

key = "epic"

def hmac_md5(msg):
	return hmac.HMAC(key, msg, sha1).hexdigest()

dic = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 _-'

for size in range(1,20):
	perm = itertools.product(dic, repeat=size)
	for w_l in perm:
		w = ''.join(w_l)
		h = hmac_md5(w)
		sys.stdout.write("\r"+h)
		if h == target_hash:
			print "Found:%s" % w
			sys.exit(0)