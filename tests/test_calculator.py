import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator(7, 2)

    def test_add(self):
        self.assertEqual(self.calc.add(), 9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(), 14)

    def test_divide(self):
        self.assertEqual(self.calc.divide(), 7/2)

    def test_power(self):
        self.assertEqual(self.calc.power(), 49)

if __name__ == '__main__':
    unittest.main()
