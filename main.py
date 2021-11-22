#!/usr/bin/env python


# function to check if x is divisible by y
def divisible(x,y):
    if y == 0:
        return "Division by zero not permitted"

    if x % y == 0:
        return True
    else:
        return False