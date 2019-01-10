def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    if len(L1) != len(L2):
        return False

    #form ditionaries for L1 and L2 with unique values as keys and
    #number of occurencies of a key as value
    dictL1 = {}
    dictL2 = {}

    setL1 = list(set(L1))
    setL2 = list(set(L2))

    if len(setL1) != len(setL2):
        return False
    
    for i in range(len(setL1)):
        dictL1[setL1[i]] = L1.count(setL1[i])
        dictL2[setL2[i]] = L2.count(setL2[i])

    if dictL1 != dictL2:
        return False

    if len(dictL1) == 0:
        return (None, None, None)
    
    keyDictL1 = list(dictL1.keys())
    valDictL1 = list(dictL1.values())
    
    maxOccurencies = max(valDictL1)
    maxKey = keyDictL1[valDictL1.index(maxOccurencies)]
    
    
    return (maxKey, maxOccurencies, type(maxKey))
    
