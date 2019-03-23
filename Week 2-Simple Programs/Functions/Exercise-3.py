# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:11:40 2019

@author: Ashmi
"""

"""
Assume following definitions have been made
"""

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

"""
1) a(False, 2, 3)
   
    returns int
    3
"""

"""
2) b(3, 2)
   
    returns int
    3
"""

"""
3) a(3>2, a, b)
   
    returns function
    function
"""

"""
3) b(a, b)
   
    returns NoneType
    error
"""



