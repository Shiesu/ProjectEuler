# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 15:49:32 2016

@author: Jan Henrik Wiik
"""

# make a list of primes using a sieve
def make_primes(upper_bound):
    nums = [0 for n in range(upper_bound+1)]
    for n in range(2, upper_bound+1):
        if nums[n]==0: nums[n] = 1
        for m in range(2, int(upper_bound/n)+1):
            nums[n*m] = 2
            
    primes = [n for n in range(len(nums)) if nums[n] == 1]
    
    return primes