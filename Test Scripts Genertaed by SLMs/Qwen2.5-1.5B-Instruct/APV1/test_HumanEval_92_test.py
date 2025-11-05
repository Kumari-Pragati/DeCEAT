system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return False


assistant

import unittest

# Importing the function from the provided code snippet
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):

    def test_any_int(self):
        # Test case 1: All inputs are integers
        self.assertTrue(any_int(5, 2, 7))
        
        # Test case 2: One input is not an integer
        self.assertFalse(any_int(3, 2, 'a'))
        
        # Test case 3: Two inputs are integers, but their sum equals the third
        self.assertTrue(any_int(3, -2, 1))
        
        # Test case 4: Inputs are floats, but they can be converted to integers
        self.assertTrue(any_int(3.6, -2.2, 2))

    def test_invalid_input_types(self):
        # Test case 5: Non-integer types for any of the inputs
        self.assertFalse(any_int('a', 2, 7))
        self.assertFalse(any_int(3, 'b', 7))
        self.assertFalse(any_int(3, 2, 'c'))

    def test_zero_sum(self):
        # Test case 6: Sum of two inputs equals the third input
        self.assertTrue(any_int(0, 0, 0))
        self.assertTrue(any_int(-1, -1, 0))
        self.assertTrue(any_int(0, 0, 0))  # This should also work as it's symmetric

    def test_negative_numbers(self):
        # Test case 7: Negative numbers
        self.assertTrue(any_int(-5, -2, 3))
        self.assertTrue(any_int(-3, -2, 1))
        self.assertTrue(any_int(-3, 2, -1))

    def test_floats_and_integers(self):
        # Test case 8: Mixed float and integer inputs
        self.assertTrue(any_int(3.6, -2.2, 2))
        self.assertTrue(any_int(-3.6, 2.2, -2))
        self.assertTrue(any_int(3.6, -2.2, -2))

    def test_edge_cases(self):
        # Test case 9: Edge cases where the conditions are met
        self.assertTrue(any_int(1, 1, 2))
        self.assertTrue(any_int(1, 2, 3))
        self.assertTrue(any_int(2, 1, 3))

if __name__ == '__main__':
    unittest.main()


This unittest test suite includes various test cases to ensure the `any_int` function behaves correctly under different scenarios, including edge cases and invalid inputs.