You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `triangle_area` function:


import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area_positive(self):
        """Test the triangle_area function with positive values"""
        self.assertAlmostEqual(triangle_area(5, 3), 7.5, delta=0.01)
        self.assertAlmostEqual(triangle_area(3, 6), 9.0, delta=0.01)
        self.assertAlmostEqual(triangle_area(4, 4), 8.0, delta=0.01)

    def test_triangle_area_zero(self):
        """Test the triangle_area function with zero height"""
        self.assertAlmostEqual(triangle_area(5, 0), 0.0, delta=0.01)

    def test_triangle_area_negative(self):
        """Test the triangle_area function with negative values"""
        self.assertRaises(ValueError, triangle_area, 5, -3)
        self.assertRaises(ValueError, triangle_area, 0, 3)
        self.assertRaises(ValueError, triangle_area, -5, 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_triangle_area_positive` tests the function with positive values for both base and height.
2. `test_triangle_area_zero` tests the function with a zero height.
3. `test_triangle_area_negative` tests the function with negative values for either base or height, which should raise a `ValueError`.

The test suite uses the `unittest.TestCase` class to define test methods and the `assertAlmostEqual` and `assertRaises` functions to verify the expected behavior of the `triangle_area` function.