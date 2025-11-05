You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_58_code import common

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))

 Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_58_code import common

class TestCommonFunction(unittest.TestCase):

    def test_common_empty_lists(self):
        self.assertListEqual(common([]), [])
        self.assertListEqual(common([], [1, 2, 3]), [])

    def test_common_single_element_lists(self):
        self.assertListEqual(common([1], [1]), [1])
        self.assertListEqual(common([1], []), [])

    def test_common_unique_elements(self):
        self.assertListEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertListEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])
        self.assertListEqual(common([1, 2, 3], [4, 5, 6]), [])

    def test_common_duplicate_elements(self):
        self.assertListEqual(common([1, 1, 2, 3], [1, 2, 3]), [1, 2, 3])
        self.assertListEqual(common([1, 2, 3], [1, 2, 3, 3]), [1, 2, 3])
        self.assertListEqual(common([1, 2, 3], [3, 2, 1]), [1, 2, 3])

    def test_common_case_insensitive(self):
        self.assertListEqual(common(["a", "b", "c"], ["A", "B", "C"]), ["A", "B", "C"])
        self.assertListEqual(common(["apple", "banana", "orange"], ["Apple", "Banana", "Orange"]), ["Apple", "Banana", "Orange"])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases, such as empty lists, single-element lists, unique elements, duplicate elements, and case-insensitive comparisons. It also checks that the function returns the elements in sorted order.