You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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
        self.assertEqual(filter_integers([0, 1, -1, 'abc', {}, []]), [0, 1, -1])

    def test_filter_integers_with_large_integers(self):
        self.assertEqual(filter_integers([1000000000, -500000000, 2000000000]), [1000000000, -500000000, 2000000000])

    def test_filter_integers_with_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_filter_integers_with_single_integer(self):
        self.assertEqual(filter_integers([42]), [42])

    def test_filter_integers_with_mixed_types_and_floats(self):
        self.assertEqual(filter_integers([1.0, 2.0, 3.0, 'abc', {}, []]), [1.0, 2.0, 3.0])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including lists with different types of elements, negative integers, zero, large integers, empty lists, and single integers. It ensures that the `filter_integers` function correctly filters out non-integer values while preserving integers of all kinds.