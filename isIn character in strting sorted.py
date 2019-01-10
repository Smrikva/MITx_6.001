

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == "":
        return False
    elif char == aStr:
        return True
    elif char < aStr[0]:
        return False
    elif char > aStr[-1]:
        return False

    if char > aStr[len(aStr)//2]:
        aStr = aStr[(len(aStr)//2+1):]
        return isIn(char, aStr)
    elif char == aStr[len(aStr)//2]:
        return True
    elif char < aStr[len(aStr)//2]:
        aStr = aStr[:len(aStr)//2]
        return isIn(char, aStr)
    else:
        return False
    
    
    
