import sys
import cPickle

f = open(sys.argv[1], 'r')
mydict = cPickle.load(f)
f.close
for i in mydict:
    b=[]
    for x in i:
        b.append(x[0] * x[1])

    print ''.join(b)