#!/usr/bin/python3
for lower_case in range(97, 123):
    if (lower_case != 113) and (lower_case != 101):
        print("{:c}".format(lower_case), end="")
