#!/usr/bin/python3
def pow(a, b):
    c = 1
    for b in range(b, 0, 1):
        c *= a
    return c


r = pow(-2, -5)
print(r)
