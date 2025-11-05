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

 Here is a simple unittest test script for the `triangle_area` function. The test cases cover the base case, edge cases, and negative inputs.


import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

    def test_edge_case_zero(self):
        self.assertEqual(triangle_area(0, 3), 0)
        self.assertEqual(triangle_area(5, 0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(triangle_area(-5, 3), 0)
        self.assertEqual(triangle_area(5, -3), 0)

if __name__ == '__main__':
    unittest.main()


You can run this script directly by saving it as a .py file and executing it using the command line:


python test_triangle_area.py


This will run the tests and provide you with the results. If all tests pass, it means the function is working as expected. If any test fails, you'll see an error message indicating which test failed and the expected and actual results.