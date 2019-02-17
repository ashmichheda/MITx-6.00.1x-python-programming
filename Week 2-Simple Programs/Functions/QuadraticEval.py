# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:59:34 2019

@author: Ashmi


Write to Python function evalQuadratic(a, b, c, x),, 
that returns the value of the quadratic. 
Calculates a*x^2 + b*x + c

This function takes in four numbers and returns to single number.

"""
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    finalVal = a*(x*x) + (b*x) + c
    return finalVal

#print(evalQuadratic(1, 1, 0, 2))
