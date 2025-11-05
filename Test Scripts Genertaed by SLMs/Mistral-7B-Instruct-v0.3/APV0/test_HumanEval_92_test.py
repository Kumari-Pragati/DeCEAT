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

 Here is a unittest test script for the `any_int` function:


import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):

    def test_any_int(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(5, 2, '7'))
        self.assertFalse(any_int('5', 2, 7))
        self.assertFalse(any_int(5, 2, [7]))
        self.assertFalse(any_int([5], 2, 7))
        self.assertFalse(any_int([5], 2, [7]))

if __name__ == '__main__':
    unittest.main()


This test script includes a `TestAnyInt` class that inherits from `unittest.TestCase`. Inside this class, there is a method `test_any_int` that tests the `any_int` function with various inputs.

The test cases cover the following scenarios:

1. When the sum of two numbers equals the third number (e.g., 5 + 2 = 7)
2. When none of the numbers equal the sum of the other two numbers (e.g., 3 + 2 ≠ 2)
3. When one of the numbers is the sum of the other two numbers (e.g., 3 + (-2) = 1)
4. When one or more of the numbers are not integers (e.g., 3.6, 2.2, 2)
5. When one or more of the numbers are not integers because they are strings (e.g., '5', 2, 7)
6. When one or more of the numbers are not integers because they are lists (e.g., [5], 2, 7)

The test script will run the tests and print the results. If all tests pass, the function is working correctly. If any tests fail, the function needs to be fixed.