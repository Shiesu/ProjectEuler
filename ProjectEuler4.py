# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 16:19:22 2016

Porject Euler #4
Time complexity: For product of two numbers under N, O(N^2).

@author: Jan Henrik Wiik
"""

import time
from math import *
start_time = time.clock()
#-----------------------------------------------------------------------------

lst= []
for n in range(900, 1000):
    for m in range(900, 1000):
        if n*m not in lst: lst.append(n*m)
palindromes = []
for N in lst:
    rev_N = int(str(N)[::-1])
    if N == rev_N:
        palindromes.append(N)
max_n =  1
for n in palindromes:
    if n > max_n:
        max_n = n
output = max_n

#-----------------------------------------------------------------------------
end_time = time.clock()
print output
print "Time elapsed: %fs"%(end_time-start_time)