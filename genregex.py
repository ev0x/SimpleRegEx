#!/usr/bin/env python
import sys

for line in sys.stdin:
    l = line.split()
    theList = []
    for i in l:
        iLen = len(i)
	if i.isalpha():
            theList.append('[a-sA-Z]{' + str(iLen) + '}')
        elif i.isdigit():
            theList.append('[0-9]{' + str(iLen) + '}')
        else:
            innerList = []
            innerLast = None
            innerCount = 1
            for s in i:
		if s.isalpha():
                    if innerLast is 'A':
                        innerCount += 1
                        innerList.pop() #remove the last item from the list
                        innerList.append('[a-zA-Z]{' + str(innerCount) + '}')
                    else:
                        innerCount = 1
                        innerList.append('[a-zA-Z]')
                    innerLast = 'A'
	        elif s.isdigit():
                    if innerLast is '1':
                        innerCount += 1
                        innerList.pop() #remove the last item from the list
                        innerList.append('[0-9]{' + str(innerCount) + '}')
                    else:
                        innerCount = 1
                        innerList.append('[0-9]')
                    innerLast = '1'

            theList.append(''.join(innerList))

    theRegEx = '\s'.join(theList)
    print "^%s$" %theRegEx
    print line
