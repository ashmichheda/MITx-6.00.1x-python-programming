# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:31:30 2019

@author: Ashmi
"""

def findGcd(a, b):
    
    if b == 0:
        return a
    else:
        return findGcd(b, a % b)

result = findGcd(8, 14)
print('Gcd is: '+str(result))