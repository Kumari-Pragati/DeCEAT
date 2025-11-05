You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the provided `median` function:


import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):

    def test_median_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertEqual(median([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(median([-10, 0, 10, 20, 30]), 0.0)
        self.assertEqual(median([-100, -50, -1, 1, 50, 100]), 0.0)

    def test_median_even_length(self):
        self.assertAlmostEqual(median([2, 3, 4, 5]), 3.5)
        self.assertAlmostEqual(median([-10, 4, 6, 1000, 10, 20, 30]), 15.0)
        self.assertAlmostEqual(median([2, 3, 4, 5, 6]), 4.0)
        self.assertAlmostEqual(median([-10, 0, 10, 20, 30, 40]), 10.0)
        self.assertAlmostEqual(median([-100, -50, -1, 1, 50, 100, 150]), 0.0)

if __name__ == '__main__':
    unittest.main()


This test suite includes two test cases: `test_median_odd_length` and `test_median_even_length`. Each test case checks the function's behavior for different input lists with odd and even lengths, respectively. The `assert*` functions are used to verify the expected output for each test case.