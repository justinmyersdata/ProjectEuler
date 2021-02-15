
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
            
def sumprime(x):
    count = 0 
    for number in range(x):
        if isprime(number):
            count+=number
    return(count)
        
sumprime(2000000)    