"""Test for main calculator startup"""
from calculator import Calculator
import pytest

def test_app_get_environment_variable():
    calculator = Calculator()
#   Retrieve the current environment setting
    current_env = calculator.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"



def test_calculator_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    calculator = Calculator()
    calculator.start()
    captured = capfd.readouterr()
    assert "Type 'exit' to exit." in captured.err  # Verify the initial print statement
