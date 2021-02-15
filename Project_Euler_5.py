# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:15:09 2021

@author: MYERSJ1
"""

def factors(x):
    factor_list = []
    factor = 2
    while x > 1:
        if x % factor == 0:
            x = x/factor
            factor_list.append(factor)
        else:
            factor +=1
    return(factor_list)
    

flist = []
for num in range(2,21):
    flist.append(factors(num))

prime_factorization = []
for num in range(2,21):
    prime_list = []
    for f in flist:
        prime_list.append(f.count(num))
    prime_factorization.append(max(prime_list))

total = 1
n = 2
for prime in prime_factorization:
    if prime != 0:
        total *= n**prime
    n+=1

print(total)