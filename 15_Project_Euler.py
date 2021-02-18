

def factorial(x):
     total = 1
     while x > 1:
          total *= x
          x -= 1
     return(total)


def lattice_paths(m,n):
     '''Returns the number of lattice paths of an m x n lattice'''

     return(int(factorial(m+n)/(factorial(m)*factorial(n))))

lattice_paths(20,20)
