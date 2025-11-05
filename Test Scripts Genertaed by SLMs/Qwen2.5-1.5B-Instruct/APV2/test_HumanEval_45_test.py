system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

# Provided function
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5, places=2)

    def test_zero_side_length(self):
        with self.assertRaises(ValueError):
            triangle_area(0, 3)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            triangle_area(5, -3)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            triangle_area('a', 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive inputs, negative inputs (to check if it handles invalid heights properly), non-integer inputs (to ensure it raises appropriate exceptions), and zero-length sides (to verify that it correctly returns `None` or raises an exception).