# https://github.com/ShriAbhinaya/lab11-AA-SB
#Partner 1: Andrea
#Partner 2: Shri
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError("Square root of negative number not allowed")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a
def logarithm(a,b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid logarithm base")
    if b <= 0:
        raise ValueError("Invalid logarithm argument")
    return math.log(b,a)
def exponent(a,b):
    return a ** b

def sub(a, b):
    return subtract(a, b)
def mul(a, b):
    return multiply(a, b)
def div(a, b):
    return divide(a, b)
def log(a, b):
    return logarithm(a, b)
def exp(a, b):
    return exponent(a, b)
