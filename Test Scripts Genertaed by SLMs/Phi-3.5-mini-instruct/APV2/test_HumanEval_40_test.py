You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_40_code import triples_sum_to_zero

class TestTriplesSumToZero(unittest.TestCase):

    def test_no_triplets_sum_to_zero(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0]), "Should return False for a list without triplets summing to zero")

    def test_triplets_sum_to_zero(self):
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 1]), "Should return True for a list with triplets summing to zero")

    def test_no_triplets_sum_to_zero_with_duplicates(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 1, -2]), "Should return False for a list with duplicates but no triplets summing to zero")

    def test_no_triplets_sum_to_zero_with_single_element(self):
        self.assertFalse(triples_sum_to_zero([1]), "Should return False for a list with a single element")

    def test_no_triplets_sum_to_zero_with_negative_numbers(self):
        self.assertFalse(triples_sum_to_zero([-1, -3, -2, 1]), "Should return False for a list with negative numbers but no triplets summing to zero")

    def test_triplets_sum_to_zero_with_positive_numbers(self):
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), "Should return True for a list with positive numbers and triplets summing to zero")

    def test_triplets_sum_to_zero_with_mixed_numbers(self):
        self.assertTrue(triples_sum_to_zero([2, -4, 5, -3, 7, -2]), "Should return True for a list with mixed numbers and triplets summing to zero")

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including lists with no triplets summing to zero, lists with triplets summing to zero, lists with duplicates, single elements, negative numbers, and mixed numbers. Each test case is designed to validate the expected behavior of the `triples_sum_to_zero` function.