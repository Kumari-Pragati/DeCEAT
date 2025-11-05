You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_8_code import sum_product


class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_elements(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, -24))

    def test_mixed_numbers(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (-2, -12))


if __name__ == '__main__':
    unittest.main()


This suite includes tests for an empty list, a list with a single element, a list with multiple elements, a list with negative numbers, and a list with mixed positive and negative numbers.

Each test uses the `assertEqual` method to check that the output of the `sum_product` function matches the expected result. If the function is correct, all these tests should pass.

Please note that the function `sum_product` is imported from the `HumanEval_8_code` module, so make sure this module is available in your Python environment.