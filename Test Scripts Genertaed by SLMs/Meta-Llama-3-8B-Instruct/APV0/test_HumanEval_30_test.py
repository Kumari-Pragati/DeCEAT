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
    return [e for e in l if e > 0]assistant

Here is the unittest test script for the `get_positive` function:

import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_positive([2, 5, 6]), [2, 5, 6])

    def test_negative_numbers(self):
        self.assertEqual(get_positive([-1, -4, -5, -3, -10]), [])

    def test_mixed_numbers(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_empty_list(self):
        self.assertEqual(get_positive([]), [])

    def test_single_negative_number(self):
        self.assertEqual(get_positive([-1]), [])

    def test_single_positive_number(self):
        self.assertEqual(get_positive([1]), [1])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestGetPositive` class with five test methods:

1. `test_positive_numbers`: Tests that the function returns the correct result when given a list of only positive numbers.
2. `test_negative_numbers`: Tests that the function returns an empty list when given a list of only negative numbers.
3. `test_mixed_numbers`: Tests that the function returns the correct result when given a list with a mix of positive and negative numbers.
4. `test_empty_list`: Tests that the function returns an empty list when given an empty list.
5. `test_single_negative_number`: Tests that the function returns an empty list when given a list with a single negative number.
6. `test_single_positive_number`: Tests that the function returns the correct result when given a list with a single positive number.

Each test method uses the `assertEqual` method to check that the result of calling `get_positive` with a specific input is equal to the expected output.

You can run this script directly to execute the tests and verify that the `get_positive` function is working correctly.