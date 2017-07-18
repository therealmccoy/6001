# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 11:07:44 2017

@author: abhishek rai

Exercise vara varb - Week 1 - MITx - 6.00.1x

Exercise:  Assume that two variables, varA and varB, are assigned values, either numbers or strings.

Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:

    "string involved" if either varA or varB are strings

    "bigger" if varA is larger than varB

    "equal" if varA is equal to varB

    "smaller" if varA is smaller than varB 
"""

if type(varA) == type ("mickey") or type(varB) == type("mickey"):
    print ("string involved")
elif varA > varB:
    print ("bigger")
elif varA == varB:
    print ("equal")
else:
    # the third statment must be true, hence
    print ("smaller")
    
    
