# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 19:20:18 2019

@author: Ashmi
"""
# Approximate Solution of finding cube root of any non-negative number

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.1
numberOfGuesses = 0

while(abs(guess**3 - cube) >= epsilon and guess <= cube):
    guess += increment
    numberOfGuesses += 1

print("No. of guessess = "+ str(numberOfGuesses))

if abs(guess **3 - cube) >= epsilon:
    print('Failed on cube root of: '+str(cube))
else:
    print(str(guess) + ' is close to the cube root of: '+str(cube))
