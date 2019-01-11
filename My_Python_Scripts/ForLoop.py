# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 21:49:09 2019

@author: Ashmi
"""
"""
for n  in range(5):
    print(n)
"""

"""
range counts sequence of integers starting from 0 and ending before 5
i.e. 0, 1, 2, 3, 4
"""

"""
mysum = 0
for i in range(7, 10):
    mysum += i
    print(mysum)
print("Out of for loop!!")
"""


"""
below for loop takes 3 arguments
1st: start index
2nd: Last index
3rd: step value increment

1, 3, 5, 7, 9 -- how i value changes after each iteration
"""
othersum = 0
for i in range(1, 10, 2):
    othersum += i
    if othersum == 4:
        break
    print(othersum)
print("Out of for loop!!")
print("BREAK!!!")