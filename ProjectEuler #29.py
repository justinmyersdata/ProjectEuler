# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:59:56 2021

@author: MYERSJ1
"""

def distinctpower(a,b):
    powers = []
    for i in range(2,a+1):
        for j in range(2,b+1):
            powers.append(i**j)
    powers = list(set(powers))
    return(len(powers))