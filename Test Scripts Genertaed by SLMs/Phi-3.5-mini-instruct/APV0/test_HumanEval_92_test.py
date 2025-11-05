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
    return False

 import unittest
from HumanEval_92_code import any_int

class TestAnyIntFunction(unittest.TestCase):

    def test_any_int_true(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertTrue(any_int(3, -2, 1))

    def test_any_int_false(self):
        self.assertFalse(any_int(3, 2, 2))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(1, 1, 3))
        self.assertFalse(any_int(-1, -2, -3))

    def test_any_int_integers(self):
        self.assertTrue(isinstance(any_int(5, 2, 7), bool))
        self.assertTrue(isinstance(any_int(3, -2, 1), bool))
        self.assertTrue(isinstance(any_int(3.6, -2.2, 2), bool))

if __name__ == '__main__':
    unittest.main()