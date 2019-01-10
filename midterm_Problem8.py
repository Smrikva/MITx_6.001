def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def f(x):
        total = 0
        for i in range(len(L)):
            ans = (L[i] * x**(len(L)-i-1))
            total += ans
        return total
    
    return f
