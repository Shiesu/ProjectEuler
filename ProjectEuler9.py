# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 17:22:43 2016

Project Euler #9
Time Complexity: 

@author: Jan Henrik Wiik
"""

import time
from math import *
start_time = time.clock()
#-----------------------------------------------------------------------------

triples = []
for m in range(1, int(sqrt(1000))):
    for n in range(1, m):
        k = 1
        while k*(2*m**2 + 2*m*n) <= 1000:
            triples.append([k*(m**2-n**2),k*2*m*n,k*(m**2+n**2)])
            k = k+1
for triple in triples:
    if sum(triple) == 1000:
        output = reduce(lambda x,y:x*y, triple)
        break
#-----------------------------------------------------------------------------
end_time = time.clock()
print output
print "Time elapsed: %fs"%(end_time-start_time)
