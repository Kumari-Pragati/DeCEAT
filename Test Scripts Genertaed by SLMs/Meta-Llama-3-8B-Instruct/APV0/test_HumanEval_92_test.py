user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given function:

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
        self.assertTrue(any_int(0, 2, 2))
        self.assertTrue(any_int(2, 0, 2))

    def test_non_integer_numbers(self):
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(3, -2.2, 1))
        self.assertFalse(any_int(3.6, -2, 2))

    def test_non_equal_numbers(self):
        self.assertFalse(any_int(3, 2, 2))
        self.assertFalse(any_int(3, 4, 5))
        self.assertFalse(any_int(2, 3, 4))

if __name__ == '__main__':
    unittest.main()


This script includes tests for positive, negative, zero, non-integer, and non-equal numbers. The `unittest.TestCase` class is used to define test cases. The `assertTrue` and `assertFalse` methods are used to check if the function returns the expected result.