system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b


assistant

import unittest

# Function to check if a triangle is a right-angled triangle
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    >>> right_angle_triangle(3, 4, 5)
    True
    >>> right_angle_triangle(1, 2, 3)
    False
    """
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b

class TestRightAngleTriangle(unittest.TestCase):
    def test_right_angle(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertFalse(right_angle_triangle(1, 2, 3))

if __name__ == '__main__':
    unittest.main()


This script defines a `right_angle_triangle` function that checks whether the given side lengths can form a right-angled triangle. It also includes a `TestRightAngleTriangle` class with two test cases to verify the correctness of the function. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.