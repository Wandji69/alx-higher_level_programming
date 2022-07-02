#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
add.__name__
sub.__name__
mul.__name__
div.__name__
a = 10
b = 5
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
