def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    result = 0
    power = 0
    while result <= num:
        power += 1
        result = base ** power
    
    diffMaxPower = base ** power - num

    diffMinPower = num - base ** (power - 1)

    if diffMaxPower < diffMinPower:
        return power
    else:
        return power-1
