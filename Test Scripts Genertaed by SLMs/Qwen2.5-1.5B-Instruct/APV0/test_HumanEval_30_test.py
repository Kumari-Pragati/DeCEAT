system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_30_code import get_positive
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e > 0]


assistant

import unittest

# Function to be tested
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):
    def test_get_positive(self):
        # Test case 1
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

        # Test case 2
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

        # Test case 3 (empty list)
        self.assertEqual(get_positive([]), [])

        # Test case 4 (all negative numbers)
        self.assertEqual(get_positive([-1, -2, -3, -4]), [])

        # Test case 5 (only one number is positive)
        self.assertEqual(get_positive([1]), [1])

if __name__ == '__main__':
    unittest.main()


This script defines a `TestGetPositive` class that inherits from `unittest.TestCase`. It contains several test cases using the `assertEqual` method to verify that the output of the `get_positive` function matches the expected results. The `if __name__ == '__main__':` block ensures that the tests can be run directly when the script is executed.