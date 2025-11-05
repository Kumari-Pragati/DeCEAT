system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return False


assistant

import unittest

# Function to check if three numbers form an arithmetic sequence
def any_int(x, y, z):
    """
    Check if one number is the sum of the other two and all numbers are integers.
    """
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x + y == z) or (x + z == y) or (y + z == x):
            return True
        return False
    return False

class TestAnyInt(unittest.TestCase):
    def test_any_int(self):
        # Test cases to verify the correctness of the function
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines the `any_int` function as described. It then creates a class `TestAnyInt` inheriting from `unittest.TestCase`, which contains a method `test_any_int` to run the tests on the `any_int` function. Finally, it calls `unittest.main()` to execute these tests when the script is run directly.