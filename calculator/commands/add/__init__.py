import sys
from decimal import Decimal
from calculator.commands import Methods  # For high-precision arithmetic
from calculator.operations import add
from calculator.commands import Command


class AddCommand(Command):
    def execute(self):
        a = Decimal(input("Enter 1st number: ").strip())
        b = Decimal(input("Enter 2nd number: ").strip())
        print(f"The result of {a} + {b} is equal to {Methods._perform_operation(a, b, add)}")
