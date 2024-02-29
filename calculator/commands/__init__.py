from abc import ABC, abstractmethod
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

class Methods():
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, with two operands, then return the result."""
        calculation = Calculation.create(a, operation, b)
        Calculations.add_calculation(calculation)
        return calculation.perform_two_operands()
    