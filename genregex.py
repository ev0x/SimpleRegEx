#!/usr/bin/env python
import sys

for line in sys.stdin:
    l = line.split()
    lLen = len(l)
    co = 0
    theList = []
    for i in l:
        iLen = len(i)
	if i.isalpha():
	    if co is 0:
	        theList.append('^[a-zA-Z]{' + str(iLen) + '}')
            elif co is lLen - 1:
                theList.append('[a-zA-Z]{' + str(iLen) + '}$')
            else:
                theList.append('[a-sA-Z]{' + str(iLen) + '}')
            co += 1
        elif i.isdigit():
            if co is 0:
                theList.append('^[0-9]{' + str(iLen) + '}')
            elif co is lLen - 1:
                theList.append('[0-9]{' + str(iLen) + '}$')
            else:
                theList.append('[0-9]{' + str(iLen) + '}')
            co += 1
        else:
            innerList = []
	    innerco = 0
            innerlLen = len(i)
            for s in i:
		if s.isalpha():
                    if innerco is 0 and co is 0: 
                        innerList.append('^[a-zA-Z]')
                    elif innerco is innerlLen - 1 and co is lLen - 1:
                        innerList.append('[a-zA-Z]$')
                    else:
                        innerList.append('[a-zA-Z]')
	        elif s.isdigit():
                    if innerco is 0 and co is 0:
                        innerList.append('^[0-9]')
                    elif innerco is innerlLen - 1 and co is lLen - 1:
                        innerList.append('[0-9]$')
                    else:
                        innerList.append('[0-9]')
                innerco += 1
            co += 1

            theList.append(''.join(innerList))

    print '\s'.join(theList)
    print line
