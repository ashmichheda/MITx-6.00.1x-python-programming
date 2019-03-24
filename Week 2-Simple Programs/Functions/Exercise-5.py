# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:11:08 2019

@author: Ashmi
"""
# Question 1
def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3)
# Answer1: 11

# Question 2
def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3, 0)
# Answer2: 1

# Question 3
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)
# Answer3: 5


# Question 4
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)
# Answer4: 3
