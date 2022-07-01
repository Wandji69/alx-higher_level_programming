#!/usr/bin/python3
def islower(c):
    i = ord(c)
    if i == 123 or i >= 97:
        print("{} => lower".format(c))
    else:
        print("{} => upper".format(str(c)))
