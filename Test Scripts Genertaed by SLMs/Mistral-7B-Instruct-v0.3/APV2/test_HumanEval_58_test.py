You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the provided function `common()`. I've followed the formatting rules and included the necessary imports.


import unittest
from HumanEval_58_code import common

class TestCommonFunction(unittest.TestCase):

    def test_common_simple_lists(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])
        self.assertEqual(common([1, 1, 1, 2, 3], [2, 1, 3]), [1, 2, 3])
        self.assertEqual(common([], []), [])
        self.assertEqual(common([1], []), [])
        self.assertEqual(common([], [1]), [])

    def test_common_one_element_lists(self):
        self.assertEqual(common([1], [1]), [1])
        self.assertEqual(common([1], [2]), [])
        self.assertEqual(common([2], [1]), [])

    def test_common_duplicates(self):
        self.assertEqual(common([1, 1, 2, 3], [2, 1, 3]), [1, 2, 3])
        self.assertEqual(common([1, 1, 2, 3], [1, 2, 1, 3]), [1, 2, 3])
        self.assertEqual(common([1, 1, 2, 3], [1, 2, 3, 1]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover various scenarios, such as simple lists, one-element lists, and lists with duplicates. It uses the `assertEqual()` method to compare the expected output with the actual output from the `common()` function.