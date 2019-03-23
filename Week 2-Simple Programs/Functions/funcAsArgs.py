# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:36:53 2019

@author: Ashmi
"""

def func_a():
    print('Inside func_a')
    
def func_b(y):
    print('Inside func_b')
    return y

def func_c(y):
    print('Inside func_c')
    return y

print(func_a())
print(5 + func_b(2))
print(func_c(func_a()))