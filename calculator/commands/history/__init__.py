from calculator.commands import Command
from calculator.calculations import Calculations

class HistoryCommand(Command):
    def execute(self, args):
        # get history
        history = Calculations.get_history()

        # print calculations
        for calculation in history:
            print(calculation)
