import unittest
from src.functions import square_root, random_integer_handler, divisible_by_input
import math

class TestFunctions(unittest.TestCase):
    def test_square_root(self):
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_random_integer_handler(self):
        for _ in range(100):
            number = random_integer_handler()
            if number % 3 == 0:
                self.assertAlmostEqual(number % 3, 0)
            if number % 4 == 0:
                self.assertEqual(number % 4, 0)
            if number > 4:
                with self.assertRaises(ValueError):
                    random_integer_handler() 


    def test_divisible_by_input(self):
        self.assertEqual(divisible_by_input(2), [2, 4, 6, 8, 10])
        self.assertEqual(divisible_by_input(3), [3, 6, 9])
        self.assertEqual(divisible_by_input(5), [5, 10])
        self.assertEqual(divisible_by_input(7), [7])
        self.assertEqual(divisible_by_input(11), [])
