# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 23:10:23 2019

@author: Ashmi
"""
# Question 1

iteration = 0
count = 0
while iteration <5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print ("Iteration" + str (iteration) + "; count is:" + str (count))
    iteration += 1 

# Q0) What is the value of the variable count that is printed out (at the printstatement) on iteration 0?

# A0) 12

# Q1) What is the value of the variable count that is printed out (at the printstatement) on iteration 1?

# A1) 24 

# Q2) What is the value of the variable count that is printed out (at the printstatement) on iteration 2?

# A2) 36
    
# Q3) What is the value of the variable count that is printed out (at the printstatement) on iteration 3?

# A3) 48

# Q4) What is the value of the variable count that is printed out (at the printstatement) on iteration 4?

# A4) 60
    
# Question 2
iteration = 0
while iteration <5:
    count = 0
    for letter in "hello, world":
        count += 1
    print ("Iteration" + str (iteration) + "; count is:" + str (count))
    iteration += 1 
    
# Q0) What is the value of the variable count that is printed out (at the printstatement) on iteration 0?

# A0) 12

# Q1) What is the value of the variable count that is printed out (at the printstatement) on iteration 1?

# A1) 12 

# Q2) What is the value of the variable count that is printed out (at the printstatement) on iteration 2?

# A2) 12
    
# Q3) What is the value of the variable count that is printed out (at the printstatement) on iteration 3?

# A3) 12

# Q4) What is the value of the variable count that is printed out (at the printstatement) on iteration 4?

# A4) 12


# Question 3
iteration = 0
while iteration <5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration% 2 == 0:
            break
    print ("Iteration" + str (iteration) + "; count is:" + str (count))
    iteration += 1 

# Q1) How many times will the printstatement be executed?
# A1) 5

# Q2) What is the largest value of the variable iterationthat will be printed out (at the printstatement)?
# A2) 4

# Q3) What is the largest value of the variable countthat will be printed out (at the printstatement)?
# A3) 12

# Q4) What is the smallest value of the variable countthat will be printed out (at the printstatement)?
# A4) one









