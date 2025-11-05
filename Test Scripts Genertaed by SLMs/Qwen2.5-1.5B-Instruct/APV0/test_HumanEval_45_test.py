system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_45_code import triangle_area
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triangle_area(a, h):
    """Given length of a side and height, return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 2.0


assistant

import unittest

# Importing the function to be tested
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area(self):
        # Test case 1: Valid inputs
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

        # Test case 2: Another valid input
        self.assertAlmostEqual(triangle_area(6, 4), 12.0)

        # Test case 3: Invalid input (non-numeric values)
        try:
            triangle_area('a', 'b')
        except TypeError as e:
            self.assertEqual(str(e), "Both sides and height must be numeric.")

        # Test case 4: Zero-length side
        try:
            triangle_area(0, 3)
        except ValueError as e:
            self.assertEqual(str(e), "Side cannot be zero or negative.")

        # Test case 5: Negative height
        try:
            triangle_area(5, -3)
        except ValueError as e:
            self.assertEqual(str(e), "Height cannot be negative.")

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and `triangle_area`, then defines a class `TestTriangleArea` that inherits from `unittest.TestCase`. It contains several test cases to verify the correctness of the `triangle_area` function. Each test case uses assertions to check if the function returns the expected results under different conditions.