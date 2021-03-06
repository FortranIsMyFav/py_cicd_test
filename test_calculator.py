"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self):
        assert 12 == calculator.multiply(4, 3)

    def test_divide(self):
        assert 3 == calculator.divide(9, 3)

    def test_pow(self):
        assert 64 == calculator.pow(8, 2)
