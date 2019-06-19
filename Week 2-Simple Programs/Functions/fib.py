# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:43:52 2019

@author: Ashmi
"""

def fibonacci(x):
    
    if x == 0 or x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

result  = fibonacci(7)
print("Fibonacci total: "+str(result))
