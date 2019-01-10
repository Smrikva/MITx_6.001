def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    setL = set(L)
    occur = 0
    res = []
    for num in setL:
        occur = L.count(num)
        if occur%2 == 0:
            continue
        else:
            res.append(num)
    try:
        return max(res)
    except ValueError:
        return None
