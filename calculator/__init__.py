#Calculator class, which utilizes calculation class to indirectly call 
#operations, so that there is only one location where user needs to interact with (i.e. this class)
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a,b,add)
        return calculation.get_result()
    
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a,b,subtract)
        return calculation.get_result()
    
    @staticmethod
    def multiply(a,b):
        calculation = Calculation(a,b,multiply)
        return calculation.get_result()
    
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a,b,divide)
        return calculation.get_result()
