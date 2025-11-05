system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_104_code import unique_digits
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    odd_digit_elements = []
    for i in x:
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)


assistant

import unittest

# Importing the function to be tested
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33], "Test case 1 failed")
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [], "Test case 2 failed")
        self.assertEqual(unique_digits([1, 2, 3, 4, 5]), [1, 3, 5], "Test case 3 failed")
        self.assertEqual(unique_digits([]), [], "Test case 4 failed")

if __name__ == '__main__':
    unittest.main()


This script imports the `unique_digits` function and defines a class `TestUniqueDigits` with a method `test_unique_digits`. It includes several test cases to verify the correctness of the `unique_digits` function. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.