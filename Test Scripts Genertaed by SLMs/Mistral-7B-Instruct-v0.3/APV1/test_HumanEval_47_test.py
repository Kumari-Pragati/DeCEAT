You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):

    def test_median_odd_length_list(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertEqual(median([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(median([-10, -5, -2, 2, 5]), -1.0)
        self.assertEqual(median([100, 200, 300, 400, 500]), 350.0)

    def test_median_even_length_list(self):
        self.assertAlmostEqual(median([2, 3, 4, 5]), 3.5)
        self.assertAlmostEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertAlmostEqual(median([-10, -5, -2, 2, 5]), -2.5)
        self.assertAlmostEqual(median([100, 200, 300, 400, 500]), 350.0)
        self.assertAlmostEqual(median([0.1, 0.2, 0.3, 0.4, 0.5]), 0.3)

    def test_empty_list(self):
        self.assertIsNone(median([]))

    def test_single_element_list(self):
        self.assertEqual(median([1]), 1)
        self.assertEqual(median([-1]), -1)
        self.assertEqual(median([0]), 0)

    def test_extreme_cases(self):
        self.assertEqual(median([float('inf'), 1, 2, 3, float('inf')]), 2)
        self.assertEqual(median([float('-inf'), -1, -2, -3, float('-inf')]), -1)
        self.assertEqual(median([float('inf'), float('inf')]), float('inf'))
        self.assertEqual(median([float('-inf'), float('-inf')]), float('-inf'))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different scenarios, such as odd and even length lists, empty lists, single-element lists, and extreme cases. It also uses `assertAlmostEqual` for testing floating-point numbers, as their precision might not be exact.