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
    