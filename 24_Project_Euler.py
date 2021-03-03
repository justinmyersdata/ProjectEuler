
from itertools import permutations

x = list(permutations('0123456789'))
permutations = []

for perm in x:
    string = ''
    for i in perm:
        string += i
    permutations.append(string)

permutations.sort()
permutations[(1000000-1)]

