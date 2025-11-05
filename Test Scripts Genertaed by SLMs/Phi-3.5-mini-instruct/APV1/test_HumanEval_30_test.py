You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_30_code import get_positive
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e > 0]

 import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_get_positive_with_mixed_numbers(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_get_positive_with_multiple_positive_numbers(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_get_positive_with_all_positive_numbers(self):
        self.assertEqual(get_positive([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_get_positive_with_all_negative_numbers(self):
        self.assertEqual(get_positive([-1, -2, -3, -4, -5]), [])

    def test_get_positive_with_zero(self):
        self.assertEqual(get_positive([0, 1, -1, 2, -2]), [1, 2])

    def test_get_positive_with_empty_list(self):
        self.assertEqual(get_positive([]), [])

    def test_get_positive_with_single_element(self):
        self.assertEqual(get_positive([1]), [1])

    def test_get_positive_with_non_integer(self):
        # Assuming the function should only work with integers
        with self.assertRaises(TypeError):
            get_positive([1.5, -2, 3])

if __name__ == '__main__':
    unittest.main()