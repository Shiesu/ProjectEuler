# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 15:21:13 2016

Project Euler #1, one line computation

@author: Jan Henrik Wiik
"""
import time
start_time = time.clock()
#-----------------------------------------------------------------------------

output = sum([m for m in range(1000) if (m % 3 == 0 or m % 5 == 0)])

#-----------------------------------------------------------------------------
end_time = time.clock()
print output
print "Time elapsed: %fs"%(end_time-start_time)