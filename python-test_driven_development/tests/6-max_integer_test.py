#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_positive_integers(self):
        """Test a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -2]), -2)

    def test_mixed_integers(self):
        """Test a list of mixed positive and negative integers"""
        self.assertEqual(max_integer([-10, 0, 10]), 10)
        self.assertEqual(max_integer([5, -5, 0]), 5)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test an empty list, which should return None"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test a list with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)
        self.assertEqual(max_integer([-1.5, -2.5, -0.5]), -0.5)

    def test_duplicates(self):
        """Test a list with duplicate values"""
        self.assertEqual(max_integer([5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 5, 5, 3]), 5)

    def test_large_numbers(self):
        """Test a list with very large numbers"""
        self.assertEqual(max_integer([10**6, 10**9, 10**3]), 10**9)

    def test_string_list(self):
        """Test a list of strings, expecting the max on ASCII values"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")

    if __name__ == '__main__':
        unittest.main()
