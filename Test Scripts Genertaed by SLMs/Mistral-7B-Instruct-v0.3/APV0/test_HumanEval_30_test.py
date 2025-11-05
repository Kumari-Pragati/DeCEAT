Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `get_positive` function:


import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_get_positive_empty_list(self):
        self.assertListEqual(get_positive([]), [])

    def test_get_positive_all_positive(self):
        self.assertListEqual(get_positive([5, 3, 2, 9, 123, 1]), [5, 3, 2, 9, 123, 1])

    def test_get_positive_all_negative(self):
        self.assertListEqual(get_positive([-1, -2, -3, -4, -5]), [])

    def test_get_positive_mixed_numbers(self):
        self.assertListEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertListEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()


This test script includes four test cases to cover different scenarios:

1. An empty list
2. A list containing only positive numbers
3. A list containing only negative numbers
4. A list containing a mix of positive and negative numbers

You can run this script directly by saving it as a .py file and running it from the command line using `python filename.py`.