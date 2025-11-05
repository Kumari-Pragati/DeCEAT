Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_47_code import median
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

 Here is a unittest test script for the provided `median` function:


import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):

    def test_median_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertEqual(median([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(median([-10, -5, -2, 2, 5]), -1.0)
        self.assertEqual(median([100, 200, 300, 400, 500]), 300.0)

    def test_median_even_length(self):
        self.assertEqual(median([2, 3, 4, 5]), 3.5)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20, 30]), 15.0)
        self.assertEqual(median([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertEqual(median([-10, -5, -2, 2, 5, 10]), -1.0)
        self.assertEqual(median([100, 200, 300, 400, 500, 600]), 350.0)

    def test_empty_list(self):
        self.assertIsNone(median([]))

    def test_single_element_list(self):
        self.assertEqual(median([1]), 1.0)
        self.assertEqual(median([-1]), -1.0)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases for different scenarios, such as odd and even length lists, negative and positive numbers, and empty and single-element lists. It also checks the edge case where the function should return None for an empty list.