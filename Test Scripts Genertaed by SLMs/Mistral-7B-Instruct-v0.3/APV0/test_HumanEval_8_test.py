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
    return sum_value, prod_value

 Here is a simple unittest test script for the `sum_product` function:


import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        self.assertEqual(sum_product([1]), (1, 1))

    def test_multiple_elements(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, 3]), (-4, 6))

if __name__ == '__main__':
    unittest.main()


This test script includes four test cases:

1. An empty list
2. A single element
3. Multiple elements (positive numbers)
4. Multiple elements with negative numbers

Each test case uses the `assertEqual` method to check if the expected output matches the actual output of the `sum_product` function. The test cases are defined within the `TestSumProduct` class, which inherits from `unittest.TestCase`. The script ends with the standard boilerplate to run the unittest module.