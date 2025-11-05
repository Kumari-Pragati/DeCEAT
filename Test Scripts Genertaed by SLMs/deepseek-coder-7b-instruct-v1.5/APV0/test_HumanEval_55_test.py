You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given Python function:


import unittest
from HumanEval_55_code import fib

class TestFib(unittest.TestCase):

    def test_fib_0(self):
        self.assertEqual(fib(0), 0)

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_8(self):
        self.assertEqual(fib(8), 21)

    def test_fib_10(self):
        self.assertEqual(fib(10), 55)

    def test_fib_15(self):
        self.assertEqual(fib(15), 610)

    def test_fib_negative(self):
        with self.assertRaises(Exception):
            fib(-1)

    def test_fib_non_integer(self):
        with self.assertRaises(Exception):
            fib(1.5)

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestFib` that inherits from `unittest.TestCase`. It includes several test methods, each of which tests a different scenario. The methods are named with the pattern `test_<description>`.

The `test_fib_0` and `test_fib_1` methods test the base cases of the function.

The `test_fib_8` and `test_fib_10` methods test the function with larger inputs.

The `test_fib_negative` and `test_fib_non_integer` methods test the function with invalid inputs. They use the `assertRaises` method to check that the function raises an exception when given invalid input.

The script ends with `unittest.main()`, which runs all the tests when the script is run directly.