You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle(self):
        # Test cases where the triangle is right-angled
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertTrue(right_angle_triangle(5, 12, 13))
        self.assertTrue(right_angle_triangle(8, 15, 17))

        # Test cases where the triangle is not right-angled
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(6, 8, 10))
        self.assertFalse(right_angle_triangle(7, 7, 7))

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case, `test_right_angle_triangle`, which tests the `right_angle_triangle` function with both right-angled and non-right-angled triangles. The `assertTrue` method is used to check that the function returns `True` for right-angled triangles, and the `assertFalse` method is used to check that the function returns `False` for non-right-angled triangles.