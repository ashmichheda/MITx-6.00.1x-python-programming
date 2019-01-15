# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 23:04:07 2019

@author: Ashmi
"""

"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
countSubstring = 0
length = len(s)
for i in range(length):
    if s[i:].startswith('bob'):
        countSubstring += 1
print('Number of times bob occurs is: '+ str(countSubstring))