# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 23:20:21 2019
@author: Ashmi
"""
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print

s = 'aabcrksbbbbbbbbadesd'
# initializing tracker variables
maxLen = 0
current = s[0]
longest = s[0]

for i in range(len(s) - 1):
    if s[i+1] >= s[i]:
        current += s[i+1]
        # if current length is bigger update
        if(len(current) > maxLen):
            maxLen = len(current)
            longest = current
    else:
        current = s[i+1]
i += 1
print('Longest substring in alphabetical order is: '+ str(longest))
