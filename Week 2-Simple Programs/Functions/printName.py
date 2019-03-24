# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:48:16 2019

@author: Ashmi
"""

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', '+ firstName)
    else:
        print(firstName, lastName)
        
# Each of the following function calls are equivalent/same

printName('Ashmi', 'Chheda', True)
printName('Eric', 'Grimson', reverse = False)
printName(lastName = "Mark", firstName = "Weins", reverse = True)