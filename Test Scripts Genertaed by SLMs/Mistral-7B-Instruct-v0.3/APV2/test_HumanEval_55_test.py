You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return fib(n - 1) + fib(n - 2)

 Here is a simple unittest test suite for the provided `fib` function. I've added some test cases to cover the base cases and a few more complex ones.


import unittest
from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)

    def test_small_numbers(self):
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)

    def test_large_numbers(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(15), 610)
        self.assertEqual(fib(20), 6765)
        self.assertEqual(fib(25), 15552)
        self.assertEqual(fib(30), 354224)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test methods: `test_base_cases`, `test_small_numbers`, and `test_large_numbers`. Each method tests the `fib` function with a specific set of inputs. The `unittest.TestCase.assertEqual` method is used to check if the expected and actual outputs match.