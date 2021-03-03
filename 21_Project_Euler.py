
def sumofdivisors(x):
    '''Returns the sum of the proper divisors of x'''
    total = 0
    
    for divisor in range(1,x//2+1):
        if x%divisor==0:
            total+=divisor
            #x = x/divisor
    return(total)
    
def divdict(x):
    '''Returns a dictionary of the sum of each divisors 
    for every integer less than x'''
    divs = {}
    
    for num in range(1,x):
        divs[num] = sumofdivisors(num)
    
    return divs



def amicablenumbers(x):
    total = 0 
    divisor = divdict(x)
    for key,value in divisor.items():
        for key1,value1 in divisor.items():
            if (key,value) == (value1,key1) and key != key1:
                #print(key,value, value1,key1)
                total += key
    return(total)
    
amicablenumbers(10000)
                