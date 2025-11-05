You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_138_code import is_equal_to_sum_even
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n % 2 == 0 and n >= 8


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):
    def test_is_equal_to_sum_even(self):
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertFalse(is_equal_to_sum_even(10))
        self.assertFalse(is_equal_to_sum_even(12))
        self.assertTrue(is_equal_to_sum_even(14))
        self.assertFalse(is_equal_to_sum_even(16))
        self.assertFalse(is_equal_to_sum_even(18))
        self.assertTrue(is_equal_to_sum_even(20))
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestIsEqualToSumEven` with a single test method `test_is_equal_to_sum_even`. This method tests the `is_equal_to_sum_even` function with a series of test cases. The `unittest.main()` at the end makes this script runnable directly.

Please note that the function `is_equal_to_sum_even` is defined to return `True` only when the input number `n` is an even number greater than or equal to 8. This means that the function will return `False` for all other even numbers, including 4, 6, 10, 12, 18, etc. This is why the test cases in the unittest script are set up as they are.

If you have a different understanding of the function's requirements, you may need to adjust the test cases accordingly.