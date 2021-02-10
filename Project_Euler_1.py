# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:47:14 2021

@author: MYERSJ1
"""

def multiples():
    '''Returns the sum of all multiples of 3 & 5 less than 100'''
    
    count = 0
    
    for num in range(0,1000):
        
        if num%5==0 or num%3==0:
            
            count+=num
    return(count)


multiples()