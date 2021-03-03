
def factorial(x):

     total = 1
     while x > 1:
          total*=x
          x-=1
     return(total)

x = factorial(100)
x = list(map(int,list(str(x))))
total = 0
for i in x:
     total+=i
print(i)


