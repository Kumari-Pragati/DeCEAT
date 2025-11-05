You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_30_code import get_positive
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e > 0]

 Here is a complete unittest test suite for the `get_positive` function:


import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_get_positive_empty_list(self):
        self.assertListEqual(get_positive([]), [])

    def test_get_positive_all_negative_list(self):
        self.assertListEqual(get_positive([-1, -2, -3]), [])

    def test_get_positive_all_positive_list(self):
        self.assertListEqual(get_positive([1, 2, 3]), [1, 2, 3])

    def test_get_positive_mixed_list(self):
        self.assertListEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_get_positive_zero_in_list(self):
        self.assertListEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()


This test suite includes five test cases to cover different scenarios:

1. An empty list
2. A list containing only negative numbers
3. A list containing only positive numbers
4. A list containing both positive and negative numbers
5. A list containing zero

Each test case uses the `assertListEqual` method to compare the expected output with the actual output of the `get_positive` function.