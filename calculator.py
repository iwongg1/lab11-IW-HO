"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Denominator cannot be 0.")

    return b / a

def log(a,b)
    if a <= 0:
        raise ValueError("Base must be larger than 0.")

    return math.log(b, a)

def exp(a, b):
    return a ** b

import math


def add(a, b):

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def log(a, b):
        if a <= 0:
            raise ValueError("Base must be larger than 0!")
        return math.log(b, a)

    def exp(a, b):
        return a ** b



