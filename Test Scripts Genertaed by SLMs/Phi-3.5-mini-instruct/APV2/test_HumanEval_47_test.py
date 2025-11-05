You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_47_code import median

class TestMedianFunction(unittest.TestCase):

    def test_odd_length_list(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_even_length_list(self):
        self.assertAlmostEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

    def test_single_element_list(self):
        self.assertEqual(median([7]), 7)

    def test_all_same_elements_list(self):
        self.assertEqual(median([5, 5, 5, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(median([-10, -5, -3, -1]), -4)

    def test_large_numbers(self):
        self.assertEqual(median([1000000, 2000000, 3000000, 4000000]), 2500000)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(median([1.5, 2.5, 3.5, 4.5]), 3.0)

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            median(['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `median` function, including:

- Lists with an odd number of elements.
- Lists with an even number of elements.
- An empty list, which should raise a `ValueError`.
- A list with a single element.
- A list with all elements being the same.
- Lists containing negative numbers.
- Lists containing large numbers.
- Lists containing floating-point numbers.
- A list containing non-numeric elements, which should raise a `TypeError`.

Each test case uses appropriate assertions to check the expected output against the actual output from the `median` function. The `assertAlmostEqual` method is used for floating-point comparisons to account for potential rounding errors.