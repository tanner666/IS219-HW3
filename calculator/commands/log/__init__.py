import sys
import calculator
from decimal import Decimal  # For high-precision arithmetic
from calculator.operations import log
from calculator.commands import Command
from calculator.commands import Methods

class LogCommand(Command):
    def execute(self):
        a = Decimal(input("Enter 1st number: ").strip())
        b = Decimal(input("Enter 2nd number: ").strip())
        print(f"The result of log {b} ({a}) is equal to {Methods._perform_operation(a, b, log)}")
