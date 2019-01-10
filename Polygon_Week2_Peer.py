# -*- coding: utf-8 -*-
"""
Created on thrusday jun 22 14:09:46 2017

@author: Khushwant
"""

def polysum (n,s) :
    import math*   #import math
    area=(0.25*n*s**2)/tan(pi/n) #area=(0.25*n*s**2)/math.tan(math.pi/n)
    per=n*s
    sum=area+per
    return sum
n=input('enter value') #n=int(input('enter value')) - input is a string, convert it to int
s=input('enter value') #s=int(input('enter value')) - input is a string, convert it to int
sid=polysum(n,s)
print (sid)
    
"""
My version:

'''
n: number of polygon sides (integer)
s: length of the polygon side

returns: sums polygon area and square of polygon perimeter
'''

import math
def polysum(n, s):
    polygonArea = (0.25*n*s**2)/(math.tan(math.pi/n))
    polygonPerimeter = n * s
    return round(polygonArea + polygonPerimeter**2, 4)
"""
