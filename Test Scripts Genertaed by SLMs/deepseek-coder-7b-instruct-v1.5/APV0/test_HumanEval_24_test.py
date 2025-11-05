You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_24_code import largest_divisor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n % i == 0:
            return i


### Response:
Here is the unittest script for the given Python function:


import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(28), 7)
        self.assertEqual(largest_divisor(100), 50)
        self.assertEqual(largest_divisor(1), 1)
        self.assertEqual(largest_divisor(1000), 500)

if __name__ == '__main__':
    unittest.main()


This script creates a test case for the `largest_divisor` function. It tests the function with a variety of inputs, including edge cases such as 1 and 1000. The `assertEqual` method is used to check that the output of the function matches the expected output. If the function is correct, all of these tests should pass.

Please note that you need to have the `HumanEval_24_code` module available in your Python environment, and the `largest_divisor` function should be defined in that module.

Also, this script assumes that the `largest_divisor` function is implemented to return the largest divisor that is smaller than the input number. If this is not the case, the tests may not behave as expected.