

def factors(x):
    '''Returns the number of divisors of x'''
    factors = 0
    for factor in range(1,int(x**(1/2))+1):
        if x%factor == 0:
            factors+=2
        if factor**2 ==x:
            factors-=1
    return(factors)
    
def triangle(x):
    '''Returns the sum of the first x integers'''
    return(int(x*(x+1)/2))



            



def trianglenumbers(fac):
    '''Returns the first triangle number with over 500 divisors'''
    '''A triangle number is the sum of the first n natural numebers'''
    '''Example the 3rd triangle number is 6'''
    on = True
    n = 1
    while on:
        if factors(triangle(n)) > fac:
            on = False
        else:
            n += 1
    return(triangle(n))

trianglenumbers(500)

    
