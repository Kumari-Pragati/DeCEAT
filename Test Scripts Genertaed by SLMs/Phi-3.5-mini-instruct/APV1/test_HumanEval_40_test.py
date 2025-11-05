You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), "Should return True for a list with triplets summing to zero")

    def test_single_element_list(self):
        self.assertFalse(triples_sum_to_zero([1]), "Should return False for a list with only one element")

    def test_empty_list(self):
        self.assertFalse(triples_sum_to_zero([]), "Should return False for an empty list")

    def test_duplicate_elements(self):
        self.assertFalse(triples_sum_to_zero([0, 0, 0]), "Should return False for a list with duplicate elements")

    def test_negative_numbers(self):
        self.assertTrue(triples_sum_to_zero([-1, -2, 1, 2]), "Should return True for a list with negative numbers")

    def test_positive_numbers(self):
        self.assertFalse(triples_sum_to_zero([1, 2, 3]), "Should return False for a list with only positive numbers")

    def test_zero_list(self):
        self.assertFalse(triples_sum_to_zero([0, 0, 0]), "Should return False for a list with all zeros")

if __name__ == '__main__':
    unittest.main()