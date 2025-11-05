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

 Here is a unittest test script for the given function `fib`. The test script checks the function's behavior for various input values and ensures that it returns the expected Fibonacci numbers.


import unittest
from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):

    def test_fib_zero(self):
        self.assertEqual(fib(0), 0)

    def test_fib_one(self):
        self.assertEqual(fib(1), 1)

    def test_fib_small_numbers(self):
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)

    def test_fib_large_numbers(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)
        self.assertEqual(fib(30), 832040)
        self.assertEqual(fib(40), 102334155)
        self.assertEqual(fib(50), 354224848179261915075)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover various input values, including small numbers, large numbers, and the edge cases of 0 and 1. The test cases use the `assertEqual` method to compare the expected and actual outputs.