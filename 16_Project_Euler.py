
def digits(x):
    '''Returns the sum of the digits of the number 2 to the power of x'''
    total = 0
    num = 2**x
    num = str(num)
    for number in num:
        total+=int(number)
    return(total)


digits(1000)