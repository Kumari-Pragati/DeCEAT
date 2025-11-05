You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_43_code import pairs_sum_to_zero
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    It returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_43_code import pairs_sum_to_zero

class TestPairsSumToZero(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertFalse(pairs_sum_to_zero([1, 3, 5, 0]))
        self.assertFalse(pairs_sum_to_zero([1, 3, -2, 1]))
        self.assertFalse(pairs_sum_to_zero([1, 2, 3, 7]))

    def test_negative_numbers(self):
        self.assertTrue(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))

    def test_single_element(self):
        self.assertFalse(pairs_sum_to_zero([1]))

    def test_empty_list(self):
        self.assertFalse(pairs_sum_to_zero([]))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

1. When the list contains positive numbers.
2. When the list contains negative numbers.
3. When the list contains a single element.
4. When the list is empty.

Each test checks whether the function returns the expected result for a specific scenario.