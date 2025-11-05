You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_52_code import below_threshold
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True

 import unittest
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_all_numbers_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_some_numbers_above_threshold(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 100))

    def test_threshold_equal_to_list_element(self):
        self.assertFalse(below_threshold([5, 5, 5], 5))

    def test_threshold_greater_than_list_element(self):
        self.assertTrue(below_threshold([1, 2, 3, 4], 5))

    def test_threshold_less_than_list_element(self):
        self.assertFalse(below_threshold([5, 6, 7, 8], 4))

    def test_list_with_negative_numbers(self):
        self.assertTrue(below_threshold([-1, -2, -3, -4], 0))

    def test_list_with_zero(self):
        self.assertTrue(below_threshold([0, 0, 0, 0], 10))

    def test_list_with_positive_numbers(self):
        self.assertTrue(below_threshold([1, 2, 3, 4], 10))

    def test_list_with_mixed_numbers(self):
        self.assertFalse(below_threshold([1, 5, 3, 2], 3))

if __name__ == '__main__':
    unittest.main()