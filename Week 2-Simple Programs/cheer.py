# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 22:53:43 2019

@author: Ashmi
"""
an_letters = "aefhilmnorsxAEFHILLMNORSX"

word = input("I will cheer for you!! Please enter a word!: ")
times = int(input("Enthusiasm level (1 - 10): "))
i = 0;

while i < len(word):
    char = word[i]
    if(char in an_letters):
        print("Give me an "+ char + "! "+ char)
    else:
        print("Give me a "+ char + "! "+ char)
    i += 1
print("What does that spell!? ")
for i in range(times):
    print(word, "!!!")
