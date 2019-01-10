def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of """        
    for i in range(len(t)):
        if type(t[i]) == int:
            continue
        else:
            t = list(t)
            try:
                t[i] = max(t[i])
                max_val(t)
            except:      
                t[i] = max_val(t[i])
    
    while type(t[0]) == list:
        t = t[0]  
    
    return max(list(t))

