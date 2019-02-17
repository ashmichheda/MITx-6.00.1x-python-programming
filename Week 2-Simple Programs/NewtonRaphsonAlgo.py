# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:05:25 2019

@author: Ashmi
"""
# Newton-Raphson
# General approximation algorithm to find roots of a polynomial in one variable

epsilon = 0.01
y = 24.0
guess = y / 2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/ (2*guess))

print('numGuesses = '+str(numGuesses))
print('Square root of '+ str(y) + ' is about '+ str(guess))