# test.py

import unittest

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(3 - 1, 2)

    def test_multiplication(self):
        self.assertEqual(2 * 3, 6)

    def test_division(self):
        self.assertEqual(6 / 2, 3)

    # def test_failure(self):
    #     # This test will intentionally fail for demonstration purposes
    #     self.assertEqual(2 + 2, 5)

if __name__ == '__main__':
    unittest.main()
