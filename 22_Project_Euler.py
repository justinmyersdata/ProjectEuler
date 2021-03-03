
import string

def namescore(file):
    '''Returns the sum of the letters in the file'''
    with open(file,'r') as f:
        names = f.read()
    
    list_names = names.replace('"','').split(',')
    list_names.sort()
    
    letters = list(string.ascii_uppercase)
    letterdict = {}
    
    for index,letter in enumerate(letters):
        letterdict[letter] = index+1

    total = 0
    i = 1  
    for name in list_names:
        score = 0
        for letter in name:
            score += letterdict[letter]
        total += (score*i)
        i+=1
    return(total)

namescore(r'C:\Users\myersj1\Desktop\names.txt')