'''Test Calculator Class'''
import pytest
from calculator import Calculator
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.log import LogCommand
import unittest
from unittest.mock import patch
from decimal import Decimal

@patch('builtins.print')
@patch('builtins.input', side_effect=['3.5', '4.5'])
def test_add_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = AddCommand()
    command.execute()
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of 3.5 + 4.5 is equal to 8.0")

@patch('builtins.print')
@patch('builtins.input', side_effect=['4.5', '3.5'])
def test_subtract_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = SubtractCommand()
    command.execute()
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of 4.5 - 3.5 is equal to 1.0")

@patch('builtins.print')
@patch('builtins.input', side_effect=['3', '4'])
def test_multiply_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = MultiplyCommand()
    command.execute()
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of 3 * 4 is equal to 12")

@patch('builtins.print')
@patch('builtins.input', side_effect=['8', '2'])
def test_divide_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = DivideCommand()
    command.execute()
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of 8 / 2 is equal to 4")

@patch('builtins.print')
@patch('builtins.input', side_effect=['8', '2'])
def test_log_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = LogCommand()
    command.execute()
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of log 2 (8) is equal to 3")