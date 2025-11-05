You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([1]), 1)
        self.assertEqual(median([1, 2]), 1.5)

    def test_even_length(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_empty_list(self):
        self.assertRaises(IndexError, median, [])

    def test_single_element(self):
        self.assertEqual(median([5]), 5)

    def test_duplicate_elements(self):
        self.assertEqual(median([1, 1, 2, 2]), 1.5)

if __name__ == '__main__':
    unittest.main()


This suite includes tests for lists of odd and even lengths, empty lists, lists with a single element, and lists with duplicate elements. It checks that the function correctly calculates the median for each of these cases.

Please note that the function `median` should be defined in a file named `HumanEval_47_code.py` for these tests to work.