user

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
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * bassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle(self):
        # Test cases where the function returns True
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertTrue(right_angle_triangle(5, 12, 13))
        self.assertTrue(right_angle_triangle(1, 1, sqrt(2)))

        # Test cases where the function returns False
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(4, 5, 6))
        self.assertFalse(right_angle_triangle(10, 10, 10))

        # Test cases with edge cases
        self.assertFalse(right_angle_triangle(0, 0, 0))
        self.assertFalse(right_angle_triangle(0, 0, 1))

    def test_edge_cases(self):
        # Test cases with edge cases
        self.assertFalse(right_angle_triangle(0, 0, 0))
        self.assertFalse(right_angle_triangle(0, 0, 1))

if __name__ == '__main__':
    unittest.main()


Note: The `sqrt(2)` in the test case `self.assertTrue(right_angle_triangle(1, 1, sqrt(2)))` is a mathematical constant, approximately equal to 1.4142135623730951.