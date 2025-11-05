user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_92_code import any_int
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    any_int(3, 2, 2) ➞ False
    any_int(3, -2, 1) ➞ True
    any_int(3.6, -2.2, 2) ➞ False
    '''

    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x + y == z) or (x + z == y) or (y + z == x):
            return True
        return False
    return Falseassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertTrue(any_int(3, -2, 1))
        self.assertTrue(any_int(2, 3, 5))

    def test_negative_numbers(self):
        self.assertTrue(any_int(-5, 2, 3))
        self.assertTrue(any_int(-3, 2, 1))
        self.assertTrue(any_int(-2, 3, 1))

    def test_zero_numbers(self):
        self.assertTrue(any_int(0, 0, 0))
        self.assertTrue(any_int(0, 1, 1))
        self.assertTrue(any_int(1, 0, 1))

    def test_non_integer_numbers(self):
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(3, 2.2, 1))
        self.assertFalse(any_int(2.5, 3, 5))

    def test_non_equal_numbers(self):
        self.assertFalse(any_int(3, 2, 2))
        self.assertFalse(any_int(3, 4, 5))
        self.assertFalse(any_int(2, 3, 4))

    def test_edge_cases(self):
        self.assertFalse(any_int(None, 2, 3))
        self.assertFalse(any_int(2, None, 3))
        self.assertFalse(any_int(2, 3, None))

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of test cases, including positive and negative numbers, zero numbers, non-integer numbers, non-equal numbers, and edge cases. Each test case is designed to test a specific aspect of the function's behavior, and the test suite as a whole provides comprehensive coverage of the function's functionality.