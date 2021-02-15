
def sumsquare(n):
    '''Returns the difference between the sum of the first n digits squared 
       and the square of the sum of the first n digits'''
    square = 0
    sumsquare = 0
    for i in range(1,n+1):
        square += i**2
        sumsquare += i
    sums = sumsquare**2
    return(sums-square)

sumsquare(100)    
    
    
