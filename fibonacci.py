#fibonacci
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-2) + fib(x-1)

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if char == aStr:
        print("ok")
        return True
    elif  len(aStr)==1:
        print("neok")
        
        return False
    elif char < aStr[len(aStr)//2]:
        aStr = aStr[0:(len(aStr)//2)]
    else:
        aStr = aStr[(len(aStr)//2):]
    print(aStr)
    isIn(char, aStr)
