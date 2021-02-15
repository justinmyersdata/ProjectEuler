
def pythagorean():
    '''Returns the product of a pythagorean triple who's sum is 1000'''
    for i in range(25):
        for j in range(25):
            a = 2*i*j
            b = j**2-i**2
            c = i**2+j**2
            if a**2+b**2 == c**2 and a+b+c==1000:
                return(a*b*c)
                
pythagorean()