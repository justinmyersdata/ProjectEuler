# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:57:43 2021

@author: MYERSJ1
"""


def digits(x):
    total = 0
    num = 2**x
    num = str(num)
    for number in num:
        total+=int(number)
    return(total)


digits(1000)