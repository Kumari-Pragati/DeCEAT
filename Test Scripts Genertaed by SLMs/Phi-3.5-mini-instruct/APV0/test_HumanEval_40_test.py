Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

    def test_empty_list(self):
        self.assertFalse(triples_sum_to_zero([]))

    def test_single_element(self):
        self.assertFalse(triples_sum_to_zero([1]))

    def test_no_zero_sum_triplets(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 7]))
        self.assertFalse(triples_sum_to_zero([2, 4, 6, 8]))

    def test_with_zero_sum_triplets(self):
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 1]))
        self.assertTrue(triples_sum_to_zero([2, -3, 1, 0]))
        self.assertTrue(triples_sum_to_zero([-1, 4, 5, -9]))
        self.assertTrue(triples_sum_to_zero([2, -4, 6, -8]))

    def test_with_zero_sum_triplets_at_end(self):
        self.assertTrue(triples_sum_to_zero([1, 3, 5, -7, 2]))
        self.assertTrue(triples_sum_to_zero([1, 3, 5, -2, 4]))

    def test_with_zero_sum_triplets_in_middle(self):
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 4, -3]))
        self.assertTrue(triples_sum_to_zero([1, 3, -4, 5, -2]))

    def test_with_zero_sum_triplets_at_beginning(self):
        self.assertTrue(triples_sum_to_zero([-1, 3, 2, 0]))
        self.assertTrue(triples_sum_to_zero([-2, 3, 1, 0]))

if __name__ == '__main__':
    unittest.main()