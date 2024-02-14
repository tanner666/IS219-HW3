'''Operations of the calculator'''
from decimal import Decimal
from math import log

# Functions are defined with type hints (statically typed for better effiency)
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def log(a: Decimal) -> Decimal:
    """Default log for base 10"""
    if a <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers")
    return Decimal(log(a))

def log(a: Decimal, base: Decimal) -> Decimal:
    """Log with special base"""
    if a <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers")
    return Decimal(log(a, base))
