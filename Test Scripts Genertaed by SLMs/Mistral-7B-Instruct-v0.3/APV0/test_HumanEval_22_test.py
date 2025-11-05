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

 Here is a unittest test script for the `filter_integers` function:


import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_single_integer(self):
        self.assertEqual(filter_integers([5]), [5])

    def test_single_non_integer(self):
        self.assertEqual(filter_integers(['a']), [])

    def test_mixed_list(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

    def test_list_of_integers(self):
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

    def test_list_of_floats(self):
        self.assertEqual(filter_integers([3.14, 5.0]), [5])

    def test_list_of_strings(self):
        self.assertEqual(filter_integers(['abc', '123']), [])

    def test_list_of_lists(self):
        self.assertEqual(filter_integers([[1, 2, 3], ['a', 'b', 4]]), [1, 2, 3, 4])

    def test_list_of_dictionaries(self):
        self.assertEqual(filter_integers([{'a': 1, 'b': 2}, {'c': 3}]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to check the function's behavior with different input types and combinations. It covers empty lists, single integers, non-integers, lists of integers, lists of floats, lists of strings, lists of lists, and lists of dictionaries.