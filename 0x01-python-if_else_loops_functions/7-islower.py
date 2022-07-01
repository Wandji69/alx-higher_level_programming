#!/usr/bin/python3
def islower(c):
    i = ord(c)
    if i == 123 or i >= 97:
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
