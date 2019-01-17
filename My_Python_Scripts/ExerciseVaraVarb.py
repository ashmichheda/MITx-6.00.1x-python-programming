# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 22:06:44 2019

@author: Ashmi
"""

# Write a piece of Python code that evaluates varA and varB, 
# and then prints out one of the following messages:
# "string involved" if either varA or varB are strings
# "bigger" if varA is larger than varB
# "equal" if varA is equal to varB
# "smaller" if varA is smaller than varB

varA = "as"
varB = "niyati"

if type(varA) == str or type(varB) == str:
    print("string involved")
    
elif varA > varB:
    print("bigger")
    
elif varA == varB:
    print("equal")
    
else:
    print("smaller")
