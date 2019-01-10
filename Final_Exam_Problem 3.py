def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    total = 0
    isNum = False
    for char in s:
        
        try:
            total += int(char)
            isNum = True
        except ValueError:
            continue
    if isNum:
        return total
    else:
        raise ValueError

            
