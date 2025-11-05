user

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
    return sorted(list(ret))assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_58_code import common

class TestCommonFunction(unittest.TestCase):

    def test_common_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])
        self.assertEqual(common([1, 2, 3], [3, 2, 1]), [1, 2, 3])
        self.assertEqual(common([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(common([1, 2, 3], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(common([], [1, 2, 3]), [])
        self.assertEqual(common([1, 2, 3], []), [])

    def test_common_elements_with_duplicates(self):
        self.assertEqual(common([1, 1, 2, 3, 3], [1, 2, 2, 3, 3]), [1, 2, 3])
        self.assertEqual(common([1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_common_elements_with_empty_lists(self):
        self.assertEqual(common([], []), [])
        self.assertEqual(common([1, 2, 3], []), [])
        self.assertEqual(common([], [1, 2, 3]), [])

    def test_common_elements_with_single_element_lists(self):
        self.assertEqual(common([1], [1]), [1])
        self.assertEqual(common([1], []), [])
        self.assertEqual(common([], [1]), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following scenarios:

- Test common elements in two lists
- Test common elements in two lists with duplicates
- Test common elements in two empty lists
- Test common elements in two lists with single elements

Each test case checks if the output of the `common` function matches the expected output.