from calculator.commands import CommandHandler
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.log import LogCommand
import multiprocessing
import pkgutil
import importlib
from calculator.commands import Command

class Calculator:

    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_commands(self):
        # Dynamically load all plugins in the plugins directory
        commands_package = 'calculator.commands'
        for _, command_name, is_pkg in pkgutil.iter_modules([commands_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                command_module = importlib.import_module(f'{commands_package}.{command_name}')
                for item_name in dir(command_module):
                    item = getattr(command_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(command_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def execute_command_in_process(self, command_name, args):
        # This method will be run by each process
        self.command_handler.execute_command(command_name, args) # pragma: no cover

    def start(self):
        self.load_commands()
        print("Type 'exit' to exit.")
        while True:
            command_input = input(">>> ").strip().split(' ')
            command_name = command_input[0]
            args = command_input[1:]
            if command_input[0].lower() == 'exit':
                break
            # Create a Process for each command execution
            process = multiprocessing.Process(target=self.execute_command_in_process, args=(command_name, args))# pragma: no cover
            process.start()# pragma: no cover
            process.join()  # Wait for the command process to finish before continuing # pragma: no cover
