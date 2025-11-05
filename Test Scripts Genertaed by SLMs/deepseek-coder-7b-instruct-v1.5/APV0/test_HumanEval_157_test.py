You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


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
        self.assertFalse(right_angle_triangle(2, 3, 4))
        self.assertFalse(right_angle_triangle(3, 4, 6))

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestRightAngleTriangle` with a single method `test_right_angle_triangle`. This method tests the `right_angle_triangle` function with a variety of inputs, both those that should return `True` and those that should return `False`. The `unittest.main()` at the end runs the test cases.

Please note that you need to have the `HumanEval_157_code` module with the `right_angle_triangle` function defined in it for this script to work. If the function is defined in a different module, you need to replace `HumanEval_157_code` with the correct module name.