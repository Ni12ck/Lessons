import math

def square(x):
    a = x**2
    print(locals())
    return a


a = 5
b = square(2)
print(b)
print(globals())