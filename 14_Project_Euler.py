# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:44:42 2021

@author: MYERSJ1
"""

def collatz(x):
    '''Returns the end of a collatz sequence'''
    if x == 1:
        return(1)
    if x%2==0:
        return(collatz(x/2))
    else:
        return(collatz(3*x+1))

collatz(5)


def count_collatz(x):
    '''Returns the number of terms in a collatz sequence'''
    count = 1
    
    while x > 1:
        if x%2==0:
            x = x/2
            count +=1
        else:
            x = 3*x+1
            count +=1
    return(count)
    
def longest_collatz(x):
    '''Returns the number that gives the longest collatz sequence less than x'''
    total = 0
    large = 0
    for num in range(x):
        if count_collatz(num) > total:
            total = count_collatz(num)
            large = num
    return(large)
    
    
longest_collatz(10**6)








    
