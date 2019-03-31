# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:55:35 2019

@author: Ashmi
"""

def odd(x):
    
    if(x % 2 == 0):
        return False
    else:
        return True


print('Is 54 an odd number? '+str(odd(54)))