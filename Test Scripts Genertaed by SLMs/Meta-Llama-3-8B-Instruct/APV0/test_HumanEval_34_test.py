user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_34_code import unique
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))assistant

Here is the unittest test script for the `unique` function:

import unittest
from HumanEval_34_code import unique

class TestUniqueFunction(unittest.TestCase):
    def test_unique(self):
        # Test with a simple list
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

        # Test with an empty list
        self.assertEqual(unique([]), [])

        # Test with a list containing duplicates
        self.assertEqual(unique([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

        # Test with a list containing non-integer values
        self.assertEqual(unique(['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])

        # Test with a list containing mixed types
        self.assertEqual(unique([1, 'a', 2, 3, 'b', 4, 5]), [1, 'a', 2, 3, 4, 5])

    def test_edge_cases(self):
        # Test with a list containing a single element
        self.assertEqual(unique([5]), [5])

        # Test with a list containing no duplicates
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestUniqueFunction` class with two test methods: `test_unique` and `test_edge_cases`. The `test_unique` method tests the function with various input lists, including a simple list, an empty list, a list with duplicates, and a list with non-integer values. The `test_edge_cases` method tests the function with edge cases, such as a list containing a single element and a list with no duplicates.

You can run this script directly to execute the tests. If all tests pass, you should see a message indicating that the tests were successful.