# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 17:03:25 2016

Project Euler #7
Time Complexity: N log(N)

@author: Jan Henrik Wiik
"""

import time
from math import *
start_time = time.clock()
#-----------------------------------------------------------------------------

N = int(3*10000*log(10000, 10)+1) # apx from prime number theorem
nums = [0 for n in range(N+1)]
for n in range(2, N+1):
    if nums[n]==0: nums[n] = 1
    for m in range(2, int(N/n)+1):
        nums[n*m] = 2
        
primes = [n for n in range(len(nums)) if nums[n] == 1]
output=primes[10000]
#-----------------------------------------------------------------------------
end_time = time.clock()
print output
print "Time elapsed: %fs"%(end_time-start_time)
