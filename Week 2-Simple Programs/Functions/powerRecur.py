# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:58:52 2019

@author: Ashmi
"""


def recurPower(base, exp):
    
    if exp <= 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

result = recurPower(4, 3)
print("Result is: "+str(result))
