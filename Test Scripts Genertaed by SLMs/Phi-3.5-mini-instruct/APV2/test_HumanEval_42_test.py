You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 import unittest
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):

    def test_increment_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_empty_list(self):
        self.assertEqual(incr_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(incr_list([10]), [11])

    def test_negative_numbers(self):
        self.assertEqual(incr_list([-1, -2, -3]), [-1, -2, -3])

    def test_zero_numbers(self):
        self.assertEqual(incr_list([0]), [1])

    def test_mixed_numbers(self):
        self.assertEqual(incr_list([-1, 0, 1, 2, -3]), [-1, 1, 2, 3, -2])

if __name__ == '__main__':
    unittest.main()