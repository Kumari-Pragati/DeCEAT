user

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
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):

    def test_median_with_even_length_list(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_median_with_odd_length_list(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_median_with_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

    def test_median_with_non_numeric_list(self):
        with self.assertRaises(TypeError):
            median(['a', 'b', 'c'])

    def test_median_with_non_list_input(self):
        with self.assertRaises(TypeError):
            median(123)

    def test_median_with_list_of_duplicates(self):
        self.assertEqual(median([1, 1, 2, 2, 3, 3]), 2)

    def test_median_with_list_of_negative_numbers(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_median_with_list_of_positive_numbers(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_median_with_list_of_mixed_numbers(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

if __name__ == '__main__':
    unittest.main()


This test suite covers various test cases, including:

- Testing with even and odd length lists
- Testing with an empty list
- Testing with non-numeric and non-list inputs
- Testing with lists of duplicates and mixed numbers
- Testing with lists of negative and positive numbers

Each test case checks the output of the `median` function against the expected result, and uses assertions to verify that the function behaves correctly in different scenarios.