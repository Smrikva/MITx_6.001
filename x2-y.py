#solves x**2 - y = 0

##epsilon = 0.00001
##y = 68
##guess = y/2.0
##numGuesses = 0
##
##while abs(guess*guess - y) >= epsilon:
##    numGuesses += 1
##    guess = guess - (((guess**2) - y)/(2*guess))
##
##print("numGuesses =", numGuesses)
##print("Square root of", y, "is about", guess)
##
##def f(x):
##    x += 1
##    print("x in f is:",x)
##    return x

print("funkcija f sa parametron y, a unutar funkcije je x")
print("\n")

def ff(y):
    x = 1
    x += 1
    print (x)

x = 5
ff(x)
print(x)

def g(y):
    print(x)
    print(x+1)

x = 5
g(x)
print(x)

def h(y):
    x += 1

x = 5
h(x)
print(x)
