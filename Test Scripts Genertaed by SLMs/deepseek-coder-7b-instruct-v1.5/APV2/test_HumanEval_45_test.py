You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

    def test_zero_height(self):
        self.assertEqual(triangle_area(5, 0), 0)

    def test_zero_side(self):
        self.assertEqual(triangle_area(0, 3), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(triangle_area(-5, 3), -7.5)

    def test_negative_height(self):
        self.assertAlmostEqual(triangle_area(5, -3), -7.5)

    def test_negative_side(self):
        self.assertAlmostEqual(triangle_area(-5, 3), -7.5)

    def test_negative_side_and_height(self):
        self.assertAlmostEqual(triangle_area(-5, -3), 7.5)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, zero height, zero side, and negative numbers. It also tests the function with negative values for both the side and the height, and with negative values for both.

Please note that the `assertAlmostEqual` method is used to compare floating point numbers. This method checks if the two numbers are close to each other, with a small tolerance.

Also, please note that the `HumanEval_45_code` module should contain the `triangle_area` function for the tests to work.