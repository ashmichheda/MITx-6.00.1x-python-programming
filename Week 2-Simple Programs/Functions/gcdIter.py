# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:27:04 2019

@author: Ashmi
"""

def findGcd(a, b):
    
    minValue = min(a, b)
    
    while a%minValue != 0 or b% minValue != 0:
        #print(minValue)
        minValue -= 1
    
    return minValue

result = findGcd(8, 14)
print('Gcd is: '+str(result))