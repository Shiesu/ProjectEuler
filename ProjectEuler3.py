# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 15:44:54 2016

@author: Jan Henrik Wiik
"""

import time
from math import *
start_time = time.clock()
#-----------------------------------------------------------------------------

# Faster to not use primes
N = 600851475143 
nums = range(2, int(sqrt(N)+1))
while N != 1:
    for n in nums:
        if N % n == 0:
            N = N/n
            if N == 1: output = n

#-----------------------------------------------------------------------------
end_time = time.clock()
print output
print "Time elapsed: %fs"%(end_time-start_time)