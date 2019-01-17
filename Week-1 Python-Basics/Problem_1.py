# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 22:55:43 2019
@author: Ashmi
"""

# Problem set 1
# Problem 1

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained 
# in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

s = 'aeiouash'
countVowel = 0
for temp in s:
    if temp == 'a' or temp == 'e' or temp == 'i' or temp == 'o' or temp == 'u':
        countVowel += 1
print('Number of vowels: '+ str(countVowel))
