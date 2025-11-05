user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_22_code import filter_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any Python values only for integers.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]assistant

Here is the unittest test script for the `filter_integers` function:

import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):
    def test_filter_integers(self):
        # Test 1: Simple case
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

        # Test 2: Mixed types
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

        # Test 3: No integers
        self.assertEqual(filter_integers(['a', 'b', 'c']), [])

        # Test 4: Only integers
        self.assertEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

        # Test 5: Mixed integers and non-integers
        self.assertEqual(filter_integers([1, 2, 'a', 3.14, 5, {'a': 1}]), [1, 2, 5])

if __name__ == '__main__':
    unittest.main()

This test script covers the following scenarios:

1. A simple case with a single integer value.
2. A mixed list of integers and non-integer values.
3. A list with no integer values.
4. A list with only integer values.
5. A mixed list of integers and non-integer values, including a dictionary.

Each test case uses the `assertEqual` method to verify that the output of the `filter_integers` function matches the expected result.