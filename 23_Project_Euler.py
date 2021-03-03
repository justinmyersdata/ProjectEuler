
def abundantnumbers():
    '''Returns the sum of all integers that can't be written as the sum of two abundant numbers'''    
    abundantnumbers = []

    for i in range(1,28123):
        total = 0
        for j in range(1,i//2+1):
            if i%j == 0:
                total+= j
        if total > i:
            abundantnumbers.append(i)
    
    sums = []
    ind = 0
    for i in abundantnumbers:
        for j in abundantnumbers[ind:]:
            sums.append(i+j)
        ind += 1
    
    sums = list(set(sums))
    
    sumtotal = 0
    for i in range(28124):
        if i in sums:
            sums.remove(i)
        else:
            sumtotal += i
    return(sumtotal)

abundantnumbers()
    