user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_42_code import incr_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]assistant

Here is the unittest test script for the `incr_list` function:

import unittest
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):
    def test_incr_list(self):
        # Test with a simple list
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

        # Test with a list of varying lengths
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

        # Test with an empty list
        self.assertEqual(incr_list([]), [])

        # Test with a list containing non-integer values
        self.assertEqual(incr_list([1, 2, 'a', 4, 5]), [2, 3, 'a', 5, 6])

        # Test with a list containing negative numbers
        self.assertEqual(incr_list([-1, 0, 1]), [0, 1, 2])

    def test_incr_list_type_error(self):
        # Test with a non-list input
        with self.assertRaises(TypeError):
            incr_list(123)

if __name__ == '__main__':
    unittest.main()

This script defines a test class `TestIncrList` with two test methods:

1. `test_incr_list`: This method tests the `incr_list` function with various inputs, including a simple list, a list of varying lengths, an empty list, a list containing non-integer values, and a list containing negative numbers. It uses the `assertEqual` method to verify that the output of the `incr_list` function matches the expected output.
2. `test_incr_list_type_error`: This method tests that the `incr_list` function raises a `TypeError` when passed a non-list input.

The script can be run directly by executing the file, and it will execute the tests and report any failures or errors.