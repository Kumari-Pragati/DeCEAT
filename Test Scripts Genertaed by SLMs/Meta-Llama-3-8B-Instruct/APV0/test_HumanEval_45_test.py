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
    return a * h / 2.0assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area(self):
        # Test with known values
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)
        self.assertAlmostEqual(triangle_area(10, 6), 30.0)
        self.assertAlmostEqual(triangle_area(2, 1), 1.0)

        # Test with negative values
        self.assertAlmostEqual(triangle_area(-5, 3), -7.5)
        self.assertAlmostEqual(triangle_area(5, -3), -7.5)

        # Test with zero values
        self.assertAlmostEqual(triangle_area(0, 0), 0.0)
        self.assertAlmostEqual(triangle_area(5, 0), 0.0)
        self.assertAlmostEqual(triangle_area(0, 3), 0.0)

        # Test with non-numeric values
        with self.assertRaises(TypeError):
            triangle_area('a', 3)
        with self.assertRaises(TypeError):
            triangle_area(5, 'b')
        with self.assertRaises(TypeError):
            triangle_area('a', 'b')

if __name__ == '__main__':
    unittest.main()


This script includes tests for the following cases:
- Known values
- Negative values
- Zero values
- Non-numeric values

The `assertAlmostEqual` method is used to compare floating point numbers, as floating point arithmetic can sometimes introduce small errors. The `assertRaises` method is used to test that the function raises a TypeError when given non-numeric values.