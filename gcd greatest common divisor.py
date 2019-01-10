def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        lower = a
        greater = b
    else:
        lower = b
        greater = a

    i = lower
    while i > 1:
        if greater % i == 0 and lower % i == 0:
            break
        i -= 1

    return i


    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if  b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
    

    
