You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_42_code import incr_list

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]

 Here is a comprehensive unittest test suite for the given Python function `incr_list`:


import unittest
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(incr_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(incr_list([1]), [2])

    def test_multiple_elements_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_negative_numbers(self):
        self.assertEqual(incr_list([-1, -2, -3]), [-0, -1, -2])

    def test_zero(self):
        self.assertEqual(incr_list([0]), [1])

    def test_large_numbers(self):
        self.assertEqual(incr_list([123]), [124])

    def test_duplicates(self):
        self.assertEqual(incr_list([3, 3, 3, 3]), [4, 4, 4, 4])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, a single-element list, multiple elements, negative numbers, zero, large numbers, and duplicates. It uses the `unittest.TestCase` class to define test methods and the `assertEqual` method to compare the expected and actual outputs.