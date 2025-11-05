system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return [x for x in values if isinstance(x, int)]


assistant

import unittest

# Importing the function to be tested
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):
    def test_filter_integers(self):
        # Test case 1: Filter out non-integer elements
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

        # Test case 2: Filter out non-integer elements including empty lists
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

        # Test case 3: Filter out non-integer elements including None
        self.assertEqual(filter_integers([None, 7, [], {}]), [])

        # Test case 4: Filter out non-integer elements including other types
        self.assertEqual(filter_integers([True, False, 0, -1, "hello"]), [0, -1])

if __name__ == '__main__':
    unittest.main()


This script defines a `TestFilterIntegers` class that inherits from `unittest.TestCase`. It contains four test cases using assertEqual methods to verify the correctness of the `filter_integers` function against provided data points. The `if __name__ == '__main__':` block ensures that the tests can be run directly when the module is executed.