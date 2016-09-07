# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 16:58:35 2016

Project Euler #6
Time Complexity: O(N)

@author: Jan Henrik Wiik
"""

import time
from math import *
start_time = time.clock()
#-----------------------------------------------------------------------------

N = 100
n = sum([m for m in range(N+1)])
n_squares = sum([m**2 for m in range(N+1)])
output = n**2 - n_squares

#-----------------------------------------------------------------------------
end_time = time.clock()
print output
print "Time elapsed: %fs"%(end_time-start_time)