

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
    
def prime(n):
    '''Returns the nth prime number'''
    count = 0
    num = 1
    while count < n:
        num +=1
        if isprime(num):
            count+=1
    return(num)
        
        

prime(10001)