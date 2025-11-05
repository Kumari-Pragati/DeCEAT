Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_157_code import right_angle_triangle
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b

 Here is a unittest test script for the provided function `right_angle_triangle`. The test cases cover various scenarios, including valid right-angled triangles, invalid right-angled triangles, and negative or zero-length sides.


import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_valid_right_angled_triangle(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertTrue(right_angle_triangle(5, 12, 13))
        self.assertTrue(right_angle_triangle(6, 8, 10))

    def test_invalid_right_angled_triangle(self):
        self.assertFalse(right_angle_triangle(3, 4, 6))
        self.assertFalse(right_angle_triangle(5, 12, 14))
        self.assertFalse(right_angle_triangle(6, 8, 11))

    def test_zero_or_negative_sides(self):
        self.assertFalse(right_angle_triangle(0, 0, 0))
        self.assertFalse(right_angle_triangle(-3, 4, 5))
        self.assertFalse(right_angle_triangle(3, -4, 5))
        self.assertFalse(right_angle_triangle(3, 4, -5))

if __name__ == '__main__':
    unittest.main()


This script includes three test methods:

1. `test_valid_right_angled_triangle`: Tests valid right-angled triangles.
2. `test_invalid_right_angled_triangle`: Tests invalid right-angled triangles.
3. `test_zero_or_negative_sides`: Tests cases with zero or negative sides.

You can run this script directly to test the `right_angle_triangle` function.