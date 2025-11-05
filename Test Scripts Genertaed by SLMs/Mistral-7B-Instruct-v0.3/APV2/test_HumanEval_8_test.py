You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return sum_value, prod_value

 Here is a complete unittest test suite for the `sum_product` function:


import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        """Test sum_product on an empty list"""
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        """Test sum_product on a list with a single element"""
        self.assertEqual(sum_product([1]), (1, 1))

    def test_multiple_elements(self):
        """Test sum_product on a list with multiple elements"""
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))
        self.assertEqual(sum_product([0, 0, 0, 0]), (0, 0))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. An empty list
2. A list with a single element
3. A list with multiple elements

Each test case checks the correctness of the `sum_product` function for the given input. The test suite uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.