You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the given Python function `right_angle_triangle`. The test suite includes several test cases to verify the function's behavior.


import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle_example(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertFalse(right_angle_triangle(1, 2, 3))

    def test_right_angle_triangle_valid_cases(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertTrue(right_angle_triangle(3, 6, 8))
        self.assertTrue(right_angle_triangle(5, 12, 13))
        self.assertTrue(right_angle_triangle(6, 8, 10))

    def test_right_angle_triangle_invalid_cases(self):
        self.assertFalse(right_angle_triangle(1, 2, 4))
        self.assertFalse(right_angle_triangle(2, 3, 6))
        self.assertFalse(right_angle_triangle(4, 3, 5))
        self.assertFalse(right_angle_triangle(5, 12, 14))
        self.assertFalse(right_angle_triangle(6, 8, 9))

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for valid right-angled triangles, invalid right-angled triangles, and edge cases. The test suite uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.