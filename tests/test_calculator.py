"""Test for main calculator startup"""
from calculator import Calculator

def test_calculator_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    calculator = Calculator()
    calculator.start()
    captured = capfd.readouterr()
    assert "Type 'exit' to exit." in captured.out  # Verify the initial print statement
