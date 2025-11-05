user

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
    return a * h / 2.0assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area_positive_values(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

    def test_triangle_area_zero_height(self):
        self.assertEqual(triangle_area(5, 0), 0)

    def test_triangle_area_zero_base(self):
        self.assertEqual(triangle_area(0, 3), 0)

    def test_triangle_area_negative_values(self):
        self.assertAlmostEqual(triangle_area(-5, -3), 7.5)

    def test_triangle_area_non_numeric_values(self):
        with self.assertRaises(TypeError):
            triangle_area('five', 3)

    def test_triangle_area_non_numeric_height(self):
        with self.assertRaises(TypeError):
            triangle_area(5, 'three')

    def test_triangle_area_non_numeric_base(self):
        with self.assertRaises(TypeError):
            triangle_area('five', 3)

    def test_triangle_area_zero_base_and_height(self):
        self.assertEqual(triangle_area(0, 0), 0)

    def test_triangle_area_non_numeric_base_and_height(self):
        with self.assertRaises(TypeError):
            triangle_area('five', 'three')

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including:

- Positive values
- Zero height
- Zero base
- Negative values
- Non-numeric values
- Zero base and height
- Non-numeric base and height

Each test case checks the output of the `triangle_area` function against the expected result. The `assertAlmostEqual` method is used to compare floating point numbers, as the result of the `triangle_area` function is a floating point number. The `assertEqual` method is used to compare integers. The `assertRaises` method is used to check if the function raises a `TypeError` when given non-numeric values.