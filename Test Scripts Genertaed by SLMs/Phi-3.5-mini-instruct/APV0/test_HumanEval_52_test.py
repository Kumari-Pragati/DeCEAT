Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

    def test_threshold_equal_to_list_elements(self):
        self.assertFalse(below_threshold([5, 5, 5], 5))

    def test_threshold_greater_than_all_elements(self):
        self.assertTrue(below_threshold([1, 2, 3, 4], 10))

    def test_threshold_less_than_all_elements(self):
        self.assertTrue(below_threshold([-1, -2, -3, -4], 0))

    def test_threshold_less_than_all_elements_with_negative_numbers(self):
        self.assertTrue(below_threshold([-10, -20, -30, -40], -25))

    def test_threshold_equal_to_all_elements(self):
        self.assertFalse(below_threshold([5, 5, 5], 5))

    def test_threshold_greater_than_all_elements_with_negative_numbers(self):
        self.assertFalse(below_threshold([-10, -20, -30, -40], -15))

if __name__ == '__main__':
    unittest.main()