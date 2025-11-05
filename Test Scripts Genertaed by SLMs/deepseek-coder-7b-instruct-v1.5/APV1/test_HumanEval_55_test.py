You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_55_code import fib

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_55_code import fib

class TestFib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(-1), None)
        self.assertEqual(fib(20), 6765)
        self.assertEqual(fib(30), 832040)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different inputs, including positive numbers, 0, and negative numbers. The expected output for negative numbers is None, as the function does not handle negative inputs.

Please note that the given function is a simple recursive implementation of the Fibonacci sequence, which is not efficient for large inputs due to its exponential time complexity. For larger inputs, a more efficient implementation would be needed.

The unittest module provides a rich set of tools for constructing and running tests. The `assertEqual` method is used to check that the actual output of the function matches the expected output. If the actual and expected outputs match, the test passes; otherwise, the test fails.

The `unittest.main()` call at the end of the script runs all the tests when the script is executed.