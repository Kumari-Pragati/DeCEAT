You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a simple unittest test suite for the `triangle_area` function. I've included some basic tests to cover the function's expected behavior.


import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area_positive(self):
        """Test the function with positive values"""
        self.assertAlmostEqual(triangle_area(5, 3), 7.5, delta=0.01)
        self.assertAlmostEqual(triangle_area(3, 6), 9.0, delta=0.01)
        self.assertAlmostEqual(triangle_area(4, 4), 8.0, delta=0.01)

    def test_triangle_area_zero(self):
        """Test the function with zero height"""
        self.assertAlmostEqual(triangle_area(1, 0), 0.0, delta=0.01)

    def test_triangle_area_negative(self):
        """Test the function with negative values"""
        self.assertRaises(ValueError, triangle_area, -1, 2)
        self.assertRaises(ValueError, triangle_area, 1, -2)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_triangle_area_positive` checks the function's behavior with positive values for both base and height.
2. `test_triangle_area_zero` checks the function's behavior with a zero height.
3. `test_triangle_area_negative` checks the function's behavior with negative values for either base or height, which should raise a `ValueError`.