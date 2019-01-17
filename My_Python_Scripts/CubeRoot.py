# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 22:13:41 2019

@author: Ashmi
"""

# Check whether number is perfect cube or not
# Use of absolute function

num = int(input("Enter a number: "))
ans = 0
while ans**3 < abs(num):
    ans = ans + 1

if ans** 3 != abs(num):
    print(str(num) +" is not a perfect cube")
else:
    if num < 0:
        ans = -ans
    print('Cube root of '+ str(num) +" is " + str(ans))
