# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:45:55 2021

@author: MYERSJ1
"""

def ispalindrome(x):
    '''Returns True if a numbers reads the same forwards as it does backwards, 
        otherwise returns False'''
    x = list(str(x))

    if len(x) == 1:
        return True
    elif len(x)%2==1:
        front = x[:len(x)//2]
        end = x[len(x)//2+1:]
    else:
        front = x[:len(x)//2]
        end = x[len(x)//2:]
    while len(front) > 0:
        if front[0] != end[-1]:
            return False
        else:
            front = front[1:]
            end = end[:-1]
    return(True)

def largepalindrome():
    '''Returns the largest palindrome that is the product of two 3 digit numbers'''
    
    p = 0
    for i in range(999,2,-1):
        for j in range(999,2,-1):
            if ispalindrome(i*j) and i*j > p:
                p = i*j
    return(p)
    
largepalindrome()