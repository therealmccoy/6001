# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 03:35:13 2017

@author: Ivon
PSET1 - Exercise 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
#initialising vowels

vowels = 0 

# including the input statement as without it, the code would not compile

word = input('Enter your word : ')

for letter in word:
    if letter == 'a' or letter == 'e' or letter == 'i' \
     or letter == 'o' or letter == 'u':
        vowels += 1 
print ('Number of vowels :' + str(vowels))


