# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:29:29 2019

@author: Ashmi
"""

low = 0
high = 100
secretNumber = int((low + high)/2)
print('Please think of a number between 0 and 100!')
status = True

while status:
        print('Is your secret number ' + str(secretNumber)+'?')
        flag = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low."
      +"Enter 'c' to indicate I guessed correctly.")

# logic to check secret number
        if flag == 'h':
            high = secretNumber
            secretNumber = int((low + high)/2)

        elif flag == 'l':
            low = secretNumber
            secretNumber = int((low + high)/2)

        elif flag == 'c':
            print('Game over. Your secret number was: '+ str(secretNumber))
            break
        else:
            print('Sorry, I did not understand your input.')