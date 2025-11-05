system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_47_code import median

class TestMedianFunction(unittest.TestCase):

    def test_median_of_odd_length_list(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_median_of_even_length_list(self):
        self.assertAlmostEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_median_of_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

    def test_median_of_non_list_input(self):
        with self.assertRaises(TypeError):
            median("Hello, World!")

    def test_median_of_list_with_duplicates(self):
        self.assertEqual(median([1, 2, 3, 2, 1]), 2)

    def test_median_of_list_with_negative_numbers(self):
        self.assertAlmostEqual(median([-10, -5, 0, 5, 10]), 0)

    def test_median_of_list_with_float_numbers(self):
        self.assertAlmostEqual(median([1.5, 2.5, 3.5, 4.5, 5.5]), 3.5)

if __name__ == '__main__':
    unittest.main()