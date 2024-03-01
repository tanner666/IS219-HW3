from calculator.commands import Command
from calculator.calculations import Calculations

class HistoryCommand(Command):
    def execute(self, args):
        # clear history
        Calculations.clear_history()

        print("History successfully cleared!")