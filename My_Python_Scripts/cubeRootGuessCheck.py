# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 22:30:16 2019

@author: Ashmi
"""

num = -27
for guess in range(abs(num) + 1):
    if guess**3 >= abs(num):
        break

if guess**3 != abs(num):
    print(num,'is not a perfect cube')
else:
    if num < 0:
        guess = -guess
    print('Cube root of '+str(num)+" is: "+ str(guess))