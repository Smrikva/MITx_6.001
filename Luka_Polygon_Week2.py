"""
n: number of polygon sides (integer)
s: length of the polygon side

returns: sums polygon area and square of polygon perimeter
"""

import math
def polysum(n, s):
    polygonArea = (0.25*n*s**2)/(math.tan(math.pi/n))
    polygonPerimeter = n * s
    return round(polygonArea + polygonPerimeter**2, 4)

n=int(input('enter value'))
s=int(input('enter value'))
sid=polysum(n,s)
print (sid)
