import unittest
from power import power

class TestPowerFunction(unittest.TestCase):
    
    def test_integer_inputs(self):
        self.assertEqual(power('a', 'b'), 'Error! Please input integer values as base and exponent.')
    
    def test_returns_power_values(self):
        self.assertEqual(power(3, 4), 81)