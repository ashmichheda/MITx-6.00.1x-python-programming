# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:56:36 2019

@author: Ashmi
"""
"""
Iteration example

Below code squares the value of x by adding it x times
"""

x = 3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft -= 1
print(str(x)+" * "+ str(x) + " = "+ str(ans))


school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        print(char)
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1
        print(numCons)

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 