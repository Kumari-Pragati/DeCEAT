You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return False


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):

    def test_integers(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(3, 2, 2))

    def test_non_integers(self):
        self.assertFalse(any_int(5.5, 2, 7))
        self.assertFalse(any_int(3, -2.2, 1))
        self.assertFalse(any_int(3, 2, 2.2))

    def test_single_integer(self):
        self.assertFalse(any_int(5, 2, 10))
        self.assertFalse(any_int(3, -2, 1))
        self.assertFalse(any_int(3, 2, 2))

    def test_negative_numbers(self):
        self.assertTrue(any_int(-5, -2, -3))
        self.assertFalse(any_int(-3, -2, 1))
        self.assertFalse(any_int(3, 2, -2))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios:

- When all numbers are integers and one of them is equal to the sum of the other two.
- When any of the numbers is not an integer.
- When only one number is an integer.
- When the numbers include negative values.

Each test case checks a specific scenario and asserts the expected output.