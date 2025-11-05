user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_8_code import sum_product
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Return a pair (sum, product) for the given list of integers.
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([])
    (0, 1)
    """
    sum_value = 0
    prod_value = 1
    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_valueassistant

Here is a unittest test script for the given Python function:

Python
import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):

    def test_sum_product(self):
        # Test with a list of integers
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
        # Test with an empty list
        self.assertEqual(sum_product([]), (0, 1))
        # Test with a list containing negative numbers
        self.assertEqual(sum_product([-1, 2, 3, 4]), (8, -24))
        # Test with a list containing zero
        self.assertEqual(sum_product([0, 1, 2, 3]), (6, 0))
        # Test with a list containing a single element
        self.assertEqual(sum_product([5]), (5, 5))
        # Test with a list containing duplicate elements
        self.assertEqual(sum_product([1, 2, 2, 3, 3, 3]), (8, 36))

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function is working correctly. It tests the function with a list of integers, an empty list, a list containing negative numbers, a list containing zero, a list containing a single element, and a list containing duplicate elements.