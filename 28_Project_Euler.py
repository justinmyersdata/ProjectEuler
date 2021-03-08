


def is_square(x):
    squares = [i*i for i in range(1,1002)]
    if x in squares:
        return True
    return False

#is_square(256)

def get_spiral(x):
    spiral = []
    small_list = []
    for num in range(1,x+1):
        small_list.append(num)
        if num % 2 == 1 and is_square(num):
            spiral.append(small_list)
            small_list = []
        elif num == x:
            spiral.append(small_list)
    return(spiral)

#spiral = get_spiral(25)

def diagonal_sum(spiral):
    total = 0
    for line in spiral:
        cycle = max(1,len(line)//4)
        for ind,num in enumerate(line[::-1]):
            if ind % cycle == 0:
                total += num
    return(total)
   
    
diagonal_sum(get_spiral(1001**2))    
        

        

