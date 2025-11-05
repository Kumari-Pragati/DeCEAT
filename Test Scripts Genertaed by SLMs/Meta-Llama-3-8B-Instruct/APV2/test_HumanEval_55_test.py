system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return fib(n - 1) + fib(n - 2)assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        self.assertEqual(fib(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fib(1), 1)

    def test_fibonacci_eight(self):
        self.assertEqual(fib(8), 21)

    def test_fibonacci_ten(self):
        self.assertEqual(fib(10), 55)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)

    def test_fibonacci_non_integer(self):
        with self.assertRaises(TypeError):
            fib(1.5)

if __name__ == '__main__':
    unittest.main()