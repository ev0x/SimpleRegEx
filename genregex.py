#!/usr/bin/env python
import sys

for line in sys.stdin:
    l = line.split()
    lLen = len(l)
    co = 0
    theList = []
    for i in l:
	if i.isalpha:
            iLen = len(i)
	    if co is 0:
	        theList.append('^[a-zA-Z]{' + str(iLen) + '}')
            elif co is lLen:
                theList.append('[a-zA-Z]{' + str(iLen) + '}')
            else:
                theList.append('[a-sA-Z]{' + str(iLen) + '}')
            co += 1
    print '\s'.join(theList)
