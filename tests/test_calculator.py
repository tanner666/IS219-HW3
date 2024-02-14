'''Test Calculator Class'''
from calculator import Calculator

def test_addition():
    '''Test that addition function works'''
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that multiplication function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that division function works '''    
    assert Calculator.divide(2,2) == 1

def test_log_one():
    '''Test that logarithm function works with one operand'''
    assert Calculator.log(100) == 2

def test_log_two():
    '''Test that logarithm function works with two operands'''
    assert Calculator.log(4,2) == 2
    