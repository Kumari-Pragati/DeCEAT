Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_71_code import triangle_area
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1.
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.

    Example:
        triangle_area(3, 4, 5) == 6.00
        triangle_area(1, 2, 10) == -1
    '''
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

 Here is a unittest test script for the `triangle_area` function:


import unittest
from HumanEval_71_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.00)
        self.assertAlmostEqual(triangle_area(6, 8, 10), 19.44)
        self.assertAlmostEqual(triangle_area(3, 6, 8), 9.00)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)
        self.assertEqual(triangle_area(3, 3, 3), -1)
        self.assertEqual(triangle_area(0, 0, 0), -1)

if __name__ == '__main__':
    unittest.main()


This test script includes two test cases: `test_valid_triangle` and `test_invalid_triangle`. The `test_valid_triangle` tests the function with valid triangle inputs and checks the results against the expected output. The `test_invalid_triangle` tests the function with invalid triangle inputs and checks that it returns -1 as expected.