# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:12:25 2019

@author: Ashmi
"""

str1 = "exterminate!"
str2 = 'number one - the larch'

print(str1.upper)
# Answer1: returns function

print(str1.upper())
# Answer2: returns String EXTERMINATE!

print(str1)
# Answer3: returns String exterminate!

print(str1.isupper())
# Answer4: returns boolean False

print(str1.islower())
# Answer5: returns boolean True

str2 = str2.capitalize()
#print(str2)
# Answer6: returns String Number one - the larch

print(str2.swapcase())
# Answer7: String nUMBER ONE - THE LARCH

print(str1.index('e'))
# Answer8: returns 0

#print(str2)
print(str2.index('n'))
# Answer9: returns 8

print(str2.find('n'))
# Answer10: returns 8

#print(str2.index('!'))
# Answer11: returns error

print(str2.find('!'))
# Answer12: returns -1

print(str1.count('e'))
# Answer13: returns 3

str1 = str1.replace('e', '*') 
print(str1)
# Answer14: returns *xt*rminat*!

print(str2.replace('one', 'seven'))
# Answer15: returns Number seven - the larch

