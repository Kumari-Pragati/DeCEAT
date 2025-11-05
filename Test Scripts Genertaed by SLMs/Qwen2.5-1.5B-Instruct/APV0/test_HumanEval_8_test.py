system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return sum_value, prod_value


assistant

import unittest

# Importing the function to be tested
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):
    
    def test_sum_product(self):
        # Test case 1: Positive integers
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
        
        # Test case 2: Empty list
        self.assertEqual(sum_product([]), (0, 1))

        # Test case 3: Negative integers
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))
        
        # Test case 4: Mixed positive and negative integers
        self.assertEqual(sum_product([5, -3, 7, -2]), (6, -14))
        
        # Test case 5: Single element list
        self.assertEqual(sum_product([10]), (10, 10))
        
        # Test case 6: Zero as an element
        self.assertEqual(sum_product([0, 1, 2, 3]), (3, 0))
        
        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()


This script imports the `sum_product` function and defines a class `TestSumProduct` that inherits from `unittest.TestCase`. It contains several test cases using assertEqual methods to verify the correctness of the `sum_product` function under different conditions. The final line calls `unittest.main()` to run all the defined tests.