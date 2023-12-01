import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator(5, 3)
        self.calc_zero = Calculator(5, 0)
        self.calc_negative = Calculator(-5, -3)

    def test_add(self):
        self.assertEqual(self.calc.add(), 8)
        self.assertIsInstance(self.calc.add(), int)

    def test_add_negative(self):
        self.assertEqual(self.calc_negative.add(), -8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), 2)
        self.assertIsInstance(self.calc.subtract(), int)

    def test_subtract_negative(self):
        self.assertEqual(self.calc_negative.subtract(), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(), 15)
        self.assertIsInstance(self.calc.multiply(), int)

    def test_multiply_negative(self):
        self.assertEqual(self.calc_negative.multiply(), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(), 5/3)
        self.assertIsInstance(self.calc.divide(), float)

    def test_divide_negative(self):
        self.assertEqual(self.calc_negative.divide(), 5/3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc_zero.divide()

    def test_power(self):
        self.assertEqual(self.calc.power(), 125)
        self.assertIsInstance(self.calc.power(), float)

    def test_power_negative(self):
        self.assertEqual(self.calc_negative.power(), -0.008)

    def test_power_zero(self):
        self.assertEqual(self.calc_zero.power(), 1)

if __name__ == '__main__':
    unittest.main()