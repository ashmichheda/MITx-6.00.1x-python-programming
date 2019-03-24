# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:12:25 2019

@author: Ashmi
"""

str1 = "exterminate!"
str2 = 'number one - the larch'

print(str1.upper)
# Answer: returns function

print(str1.upper())
# Answer: returns String EXTERMINATE!

print(str1)
# Answer: returns String exterminate!

print(str1.isupper())
# Answer returns boolean False

print(str1.islower())
# Answer returns boolean True

str2 = str2.capitalize()
#print(str2)
# Answer returns String Number one - the larch

print(str2.swapcase())
# returns String nUMBER ONE - THE LARCH

print(str1.index('e'))
# Answer returns 0

print(str2)
print(str2.index('n'))
# Answer returns 8

print(str2.find('n'))
# Answer returns 8

#print(str2.index('!'))
# Answer returns error

print(str2.find('!'))
# Answer returns -1

print(str1.count('e'))
# Answer returns 3

str1 = str1.replace('e', '*') 
print(str1)
# Answer returns *xt*rminat*!

print(str2.replace('one', 'seven'))
# Answer returns Number seven - the larch


