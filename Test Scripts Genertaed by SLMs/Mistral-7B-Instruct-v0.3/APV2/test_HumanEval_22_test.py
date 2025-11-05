You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `filter_integers` function:


import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(filter_integers([]), [])

    def test_list_with_integers(self):
        self.assertListEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_only_integers(self):
        self.assertListEqual(filter_integers([1, 2, 3]), [1, 2, 3])

    def test_list_with_floats(self):
        self.assertListEqual(filter_integers([3.14, 4.56, 5]), [5])

    def test_list_with_strings(self):
        self.assertListEqual(filter_integers(['a', 'b', '5']), ['5'])

    def test_list_with_mixed_types(self):
        self.assertListEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, lists with only integers, lists with floats, lists with strings, and lists with mixed types. The `assertListEqual` method is used to verify that the expected and actual output match.