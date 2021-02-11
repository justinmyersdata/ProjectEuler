
def fibo():
    '''Returns the sum of all even fibonacci numbers less than 4,000,000'''
    
    fibo_old = 0
    
    fibo_new = 1
    
    fibo_sum = 0
    
    while fibo_new <= 4000000:
        
        fibo_new, fibo_old = fibo_old + fibo_new, fibo_new
        
        if fibo_new % 2 == 0:
            
            fibo_sum += fibo_new
    
    return(fibo_sum)
    
fibo()
          

    
