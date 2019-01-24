# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:17:55 2019

@author: Ashmi
"""

# Exercise - 2
# Question 1
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

# Select the answer that best describes what occurs when the above code is executed:
# Answer: Script enters an infinite loop and never terminates

# Question 2
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

# Select the answer that best describes what occurs when the above code is executed:
# Answer: Script successfully completes, and prints out succeeded: 4.9999999999998 (or succeeded: 5.0) 

# Question 3

# Given the above same code, but the first line changed to x = 23
# Answer: Script successfully completes, but prints out failed  