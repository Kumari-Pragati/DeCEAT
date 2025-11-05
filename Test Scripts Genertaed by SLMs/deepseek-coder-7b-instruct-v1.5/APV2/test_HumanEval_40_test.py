You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_40_code import triples_sum_to_zero
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    It returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_40_code import triples_sum_to_zero

class TestTriplesSumToZero(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 7]))

    def test_negative_numbers(self):
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))

    def test_single_element(self):
        self.assertFalse(triples_sum_to_zero([1]))

    def test_zero_in_list(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0]))

    def test_two_elements(self):
        self.assertFalse(triples_sum_to_zero([1, 3]))

    def test_three_elements_sum_to_zero(self):
        self.assertTrue(triples_sum_to_zero([1, -1, 0]))

    def test_large_list(self):
        self.assertTrue(triples_sum_to_zero([i for i in range(-1000, 1000, 2)]))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios:

- When the list contains positive numbers
- When the list contains negative numbers
- When the list contains a single element
- When the list contains a zero
- When the list contains two elements
- When the list contains three elements that sum to zero
- When the list is a large list of numbers from -1000 to 1000 with a step of 2

Each test case checks the output of the `triples_sum_to_zero` function with a specific input.