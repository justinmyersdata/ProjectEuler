

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



def order(x):
    '''Fermats little theorem'''
    k = 2
    while pow(10,k,x) != 1:
        k += 1
    if k == x-1:
        return True
    else:
        return False

def cycle_finder(x):
    
    prime_list = []
    
    for num in range(1,x):
        if isprime(num):
            prime_list.append(num)
    
    for prime in prime_list[::-1]:
        if order(prime):
            return(prime)


cycle_finder(1000)