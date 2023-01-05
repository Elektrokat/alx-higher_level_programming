#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_dg = number % 10
    else:
        last_dg = (number * -1) % 10
    print("{:d}".format(last_dg), end="")
    return (last_dg)
