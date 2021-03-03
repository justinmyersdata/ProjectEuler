
def fibo(x):
    f1 = 1
    f2 = 1
    while x > 2:
        f2,f1 = f2+f1,f2
        x -= 1
    return(f2)
    
def longfibo():
    flag = True
    x = 1
    while flag:
        if len(str(fibo(x))) >=1000:
            flag = False
        else:
            x+=1
    return(x)
    
longfibo()
