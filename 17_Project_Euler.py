

def singlewordcount(x):
     if x in [4,5,9]:
          return 4
     elif x in [1,2,6]:
          return 3
     elif x in [3,7,8]:
          return 5
     else:
          return 0

def doubleword(x):
     if x < 10:
          return(singlewordcount(x))
     elif x < 20:
          if x == 10:
               return 3
          elif x in [11,12]:
               return 6
          elif x in [13,14,19,18]:
               return 8
          elif x in [15,16]:
               return 7
          elif x in [17]:
               return 9
     else:
          if x//10 in [2,3,8,9]:
               return 6 + singlewordcount(x%10)
          elif x//10 in [4,5,6]:
               return 5 + singlewordcount(x%10)
          elif x//10 in [7]:
               return 7 + singlewordcount(x%10)
          else:
               return 0

def tripleword(x):
     if x == 1000:
          return 11
     elif x < 100:
          return(doubleword(x))
     else:
          if x%100 == 0:
               return (singlewordcount(x//100)+7)
          else:
               return(singlewordcount(x//100)+10+doubleword(x%100))

total = 0
for i in range(1,1001):
     total += tripleword(i)
     print(i, tripleword(i),total)



