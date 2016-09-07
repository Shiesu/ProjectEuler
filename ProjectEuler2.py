# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 15:21:13 2016

Project Euler #2

@author: Jan Henrik Wiik
"""
import time
start_time = time.clock()
#-----------------------------------------------------------------------------

f1, f2, output = 1, 2, 0
while f1 < 4*10**6:
    if f1 % 2 == 0: output += f1
    if f2 % 2 == 0: output += f2
    f1, f2 = f1 + f2, f1+2*f2

#-----------------------------------------------------------------------------
end_time = time.clock()
print output
print "Time elapsed: %fs"%(end_time-start_time)

