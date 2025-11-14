# https://github.com/ShriAbhinaya/lab11-AA-SB
#Partner 1: Andrea
#Partner 2: Shri

import math
import unittest
from calculator import(add, subtract, multiply, divide, logarithm, exponent, square_root, hypotenuse)

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

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
