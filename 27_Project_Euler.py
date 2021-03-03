
def isprime(x):
    '''Returns True if x is prime and false if x is composite'''
    if x < 1:
        return False
    
    elif x == 1:
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

def polyeval(poly,x):
    '''Evaluates a polynomial at point x'''
    exp = len(poly)-1
    total = 0
    for co in poly:
        total += co*x**exp
        exp-=1
    return(total)


def primecounter(poly):
    
    flag = True
    x = 0
    total = 0
    while flag:
        if isprime(polyeval(poly,x)):
            total+=1
            x+=1
        else:
            flag = False
    return(total)

#primecounter([1,-79,1601])

def max_prime_poly():
    primes = []
    
    for num in range(1,1000):
        if isprime(num):
            primes.append(num)
    
    max_primes = 0
    poly = []
    for a in range(-999,1000):
        for prime in primes:
            if primecounter([1,a,prime]) > max_primes:
                max_primes = primecounter([1,a,prime])
                poly = [1,a,prime]
    return(poly)
    
max_prime_poly()
            

        
        
        