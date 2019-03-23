# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:52:01 2019

@author: Ashmi
"""

def g(x):
    def h():
        x = "abc"
    x = x + 1
    print('in g(x): x = ',x)
    h()
    return x

x = 3
z = g(x)