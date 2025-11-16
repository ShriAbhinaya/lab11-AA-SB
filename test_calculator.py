# https://github.com/ShriAbhinaya/lab11-AA-SB
#Partner 1: Andrea
#Partner 2: Shri Abhinaya

import math
import unittest
from calculator import(add, subtract, multiply, divide, logarithm, exponent, square_root, hypotenuse)

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-5, 2), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-4, -6), 2)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(divide(2,10), 5.0)
        self.assertAlmostEqual(divide(-2,8), -4.0)
        with self.assertRaises(ZeroDivisionError):
            divide(0,10)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), math.log(100, 10))
        self.assertAlmostEqual(logarithm(2, 8), math.log(8, 2))
        self.assertAlmostEqual(log(10, 100), math.log(100, 10))

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    ######## Partner 1#######
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

        with self.assertRaises(ValueError):
            logarithm(-2, 8)

        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-1)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
