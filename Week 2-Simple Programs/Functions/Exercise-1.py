# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:46:43 2019

@author: Ashmi

Part 1: Function Types

For each of the following functions, specify the type of its return. 
You can assume each function is called with an appropriate argument, 
as specified by its docstring.

If the output can be either an int or a float, select num, which isn't a real Python type, 
but which we'll use to indicate that either basic numeric type is legal.

"""
# Q1 Indicate the type of the output that the function a will yield.
def a(x):
   '''
   x: int or float.
   '''
   return x + 1

#A1: num

# Q2 Indicate the type of the output that the function b will yield.
   def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0

#A2: flaot
   
# Q3 Indicate the type of the output that the function c will yield.
 def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

#A3: num
   
# Q4 Indicate the type of the output that the function d will yield.
def d(x, y):
   '''
   x: Can be int or float.
   y: Can be int or float.
   '''
   return x > y

#A4: boolean


# Q5 Indicate the type of the output that the function e will yield.
def e(x, y, z):
   '''
   x: Can be int or float.
   y: Can be int or float.
   z: Can be int or float.
   '''
   return x >= y and x <= z

#A5: boolean


# Q6 Indicate the type of the output that the function f will yield.
def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2

#A6: NoneType

