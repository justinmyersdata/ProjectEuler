
def isprime(x):
    '''Returns True if x is prime and false if x is composite'''
    
    if x == 1:
        return False
    
    elif x == 2:
        return True
    
    elif x % 2 == 0:
        return False
    
    else:
        for y in range(3,int(x**(1/2))+1,2):    
            if x % y == 0:        
                return False
        return True
            
            
        
        
def largeprime(x):
    '''Returns the largest prime factor of a number'''
    
    prime_factors = []
    n = 2
    while x > 1:
        if x % n == 0 and isprime(n):    
            prime_factors.append(n)    
            x = x/n
        n += 1
    
    return(max(prime_factors))
    
largeprime(600851475143)


        
