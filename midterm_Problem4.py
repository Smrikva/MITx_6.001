def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    i = 0
    ans = 0
    while ans < k:
        i += 1
        ans += i
        print(i, "ans je:", ans)
    if ans == k:
        return True
    else:
        return False
        
