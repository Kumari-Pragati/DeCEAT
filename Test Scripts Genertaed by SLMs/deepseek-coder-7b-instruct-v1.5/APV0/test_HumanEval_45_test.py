You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

    def test_zero_height(self):
        self.assertEqual(triangle_area(5, 0), 0)

    def test_zero_base(self):
        self.assertEqual(triangle_area(0, 3), 0)

    def test_negative_values(self):
        self.assertAlmostEqual(triangle_area(-5, 3), -7.5)

    def test_negative_height(self):
        self.assertAlmostEqual(triangle_area(5, -3), -7.5)

    def test_negative_base_and_height(self):
        self.assertAlmostEqual(triangle_area(-5, -3), 7.5)

if __name__ == '__main__':
    unittest.main()


This script tests the `triangle_area` function with various input combinations, including positive values, zero height or base, and negative values. It uses `assertAlmostEqual` to compare floating-point results, and `assertEqual` for integer results.

Please note that the `HumanEval_45_code` module should contain the `triangle_area` function for this script to work.

You can run this script directly in a Python environment to test the `triangle_area` function. If all tests pass, it means that the function is working correctly. If any test fails, it indicates that the function is not working as expected.