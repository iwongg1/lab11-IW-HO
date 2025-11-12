# https://github.com/iwongg1/lab11-IW-HO
# Partner 1: Isabella Wong
# Partner 2: Holly Overholser

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######## Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 6), 11)
        self.assertEqual(add(3, -1), 2)

    def test_subtract(self):
        self.assertEqual(sub(5, 2), 3)
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(6, 7), -1)
    ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(2, -4), -8)
        self.assertEqual(mul(-6, -4), 24)
        self.assertEqual(mul(5, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3,6), 2)
        self.assertEqual(div(-3, 9), -3)
        self.assertEqual(div(-2, -8), 4)
    ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)
        with self.assertRaises(ValueError):
            log(-2, 5)
        with self.assertRaises(ValueError):
            log(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2.25), 1.5)
    #########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(log(10, 100), 2)
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(3, 9), 2)


    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(0, 6)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()