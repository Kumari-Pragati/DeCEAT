You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers_with_mixed_types(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

    def test_filter_integers_with_only_integers(self):
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

    def test_filter_integers_with_no_integers(self):
        self.assertEqual(filter_integers(['a', 'b', 'c']), [])

    def test_filter_integers_with_negative_integers(self):
        self.assertEqual(filter_integers([-1, -2, -3, 'abc', {}, []]), [-1, -2, -3])

    def test_filter_integers_with_zero(self):
        self.assertEqual(filter_integers([0, 1, 2, 'abc', {}, []]), [0, 1, 2])

    def test_filter_integers_with_large_integers(self):
        self.assertEqual(filter_integers([1000000000, 2000000000, -3000000000, 'abc', {}, []]),
                         [1000000000, 2000000000, -3000000000])

    def test_filter_integers_with_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_filter_integers_with_single_integer(self):
        self.assertEqual(filter_integers([42]), [42])

    def test_filter_integers_with_non_integer_objects(self):
        self.assertEqual(filter_integers([1.0, 2.0, 3.0, 4.0]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()