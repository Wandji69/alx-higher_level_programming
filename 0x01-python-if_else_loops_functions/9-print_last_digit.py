#!/usr/bin/python3
def print_last_digit(number):
    i = number % 10
    return f"{i}{i}"


r = print_last_digit(98)
print(r)
