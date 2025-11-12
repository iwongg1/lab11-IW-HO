"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        result = math.sqrt(a)
    except ValueError:
        print("Must be greater than or equal to 0!")
    return result

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return b / a

    def log(a, b):
        if a <= 0:
            raise ValueError("Base must be larger than 0!")
        return math.log(b, a)

    def exp(a, b):
        return a ** b


