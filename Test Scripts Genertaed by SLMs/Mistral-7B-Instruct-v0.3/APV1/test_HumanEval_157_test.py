You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a simple unittest test suite for the given Python function `right_angle_triangle`. I've included some test cases to cover the basic functionality and edge cases.


import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(5, 12, 13))  # Pythagorean triple
        self.assertFalse(right_angle_triangle(4, 3, 5))  # Reversed sides
        self.assertFalse(right_angle_triangle(0, 0, 0))  # Zero sides
        self.assertFalse(right_angle_triangle(1, 1, 2))  # Not a right-angled triangle
        self.assertFalse(right_angle_triangle(2, 4, 5))  # One side is greater than the sum of the other two

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the correct behavior of the function, edge cases, and invalid inputs. The test cases are self-explanatory, and you can modify them as needed to cover additional scenarios.