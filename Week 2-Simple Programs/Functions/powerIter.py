# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:52:56 2019

@author: Ashmi
"""

def iterPower(base, exp):
    
    # when exp is 0, result will be 1 by default
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
    return result

result = iterPower(2, 0)
print("Result is: "+str(result))
