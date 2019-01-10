def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    dKeys = list(d.keys())
    dValues = list(d.values())
    
    copyDict = d.copy()
    #get unique dictionary values 
    set_dValues = set(dValues)
    
    #loop through dict and append unique values as keys to inverse dict
    inverseDict = {}
    for val in set_dValues:
        inverseDict[val] = []

    #append keys as values to the inverse dict
    for key in dKeys:
        inverseDict[copyDict.pop(key)].append(key)

    for i in inverseDict.keys():
        inverseDict[i].sort()
    return inverseDict
                
