#!/usr/bin/env python3

''' Think Python
'''

def printall(*args):
    print(args)
    
'''
In [2]: printall(1, 2, '3')
(1, 2, '3')
'''

''' Write a function called sumall that takes any number of arguments
    and returns their sum'''
    
def sumall(*args):
    total = 0
    for entry in args:
        total += entry
    return total

# $ToDo single-line comprehension