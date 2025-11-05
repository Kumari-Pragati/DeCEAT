system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


assistant

import unittest

# Importing the function from the given module
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle(self):
        # Test cases to verify the correctness of the right_angle_triangle function
        self.assertTrue(right_angle_triangle(3, 4, 5))  # Expected True
        self.assertFalse(right_angle_triangle(1, 2, 3))  # Expected False
        self.assertTrue(right_angle_triangle(5, 12, 13))  # Expected True
        self.assertFalse(right_angle_triangle(6, 8, 10))  # Expected True
        self.assertTrue(right_angle_triangle(7, 24, 25))  # Expected True
        self.assertFalse(right_angle_triangle(10, 6, 8))  # Expected False

if __name__ == '__main__':
    unittest.main()


This solution includes a `unittest` test case that covers various scenarios to ensure the `right_angle_triangle` function behaves as expected according to its docstring.