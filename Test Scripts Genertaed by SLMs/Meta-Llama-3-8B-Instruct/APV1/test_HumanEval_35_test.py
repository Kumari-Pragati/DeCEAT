user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_35_code import max_element
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return massistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):

    def test_max_element_positive_numbers(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_max_element_negative_numbers(self):
        self.assertEqual(max_element([-5, -3, -10]), -5)

    def test_max_element_mixed_numbers(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_max_element_empty_list(self):
        with self.assertRaises(IndexError):
            max_element([])

    def test_max_element_single_element_list(self):
        self.assertEqual(max_element([5]), 5)

    def test_max_element_list_with_duplicates(self):
        self.assertEqual(max_element([1, 2, 2, 3, 3, 3]), 3)

    def test_max_element_list_with_negative_duplicates(self):
        self.assertEqual(max_element([-5, -5, -5, -10, -10]), -5)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including:

- Positive numbers
- Negative numbers
- Mixed numbers
- Empty list
- Single-element list
- List with duplicates
- List with negative duplicates

Each test case checks if the function returns the expected result. The `assertEqual` method is used to compare the actual output with the expected output. The `assertRaises` method is used to check if the function raises an `IndexError` when an empty list is passed.