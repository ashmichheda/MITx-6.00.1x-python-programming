# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:10:26 2019

@author: Ashmi
"""
cube = 27
epsilon = 0.01
numGuesses = 0
low = 0.0
high = cube
ans = (low + high)/2.0

while abs(ans**3 - cube) >= epsilon:
    print('low = ' + str(low)+' high = '+ str(high) + 'ans = '+ str(ans))
    numGuesses += 1
    if ans**3 < cube:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
print('No. of guessess = '+ str(numGuesses))
print(str(ans) + ' is close to cube root of '+ str(cube))