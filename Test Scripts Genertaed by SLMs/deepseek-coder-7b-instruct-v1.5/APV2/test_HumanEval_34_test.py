You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_34_code import unique
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_34_code import unique

class TestUnique(unittest.TestCase):

    def test_unique_elements(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_single_element_list(self):
        self.assertEqual(unique([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(unique([1, 1, 1, 1]), [1])

    def test_sorted_list(self):
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(unique([5, 3, 2, 9, 0]), [0, 2, 3, 5, 9])

    def test_negative_numbers(self):
        self.assertEqual(unique([-5, -3, -5, -2, -3, -3, -9, 0, -123]), [-123, -9, -5, -3, -2, 0])

if __name__ == '__main__':
    unittest.main()


This suite includes tests for various scenarios including:

- A list with unique elements
- An empty list
- A list with a single element
- A list with duplicate elements
- A sorted list
- An unsorted list
- A list with negative numbers

Each test checks if the output of the `unique` function matches the expected result.