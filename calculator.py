# https://github.com/iwongg1/lab11-IW-HO
# Partner 1: Isabella Wong
# Partner 2: Holly Overholser


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Must be greater than or equal to 0!")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        result = b / a
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by 0!")
    return result

def log(a, b):
    if a <= 0:
        raise ValueError("Base must be larger than 0!")
    if b <= 0:
        raise ValueError("Argument must be larger than 0!")
    return math.log(b, a)

def exp(a, b):
    return a ** b



