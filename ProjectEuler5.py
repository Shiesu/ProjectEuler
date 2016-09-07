# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 16:53:02 2016

Project Euler #5
Time Complexity: O(1)

@author: Jan Henrik Wiik
"""

import time
from math import *
start_time = time.clock()
#-----------------------------------------------------------------------------

output = 16*9*5*7*11*13*17*19
#-----------------------------------------------------------------------------
end_time = time.clock()
print output
print "Time elapsed: %fs"%(end_time-start_time)