You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_46_code import fib4

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]

 Here is a comprehensive unittest test suite for the given Python function `fib4`. The test suite includes a variety of test cases to ensure the function works correctly for different inputs.


import unittest
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):

    def test_fib4_base_cases(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)

    def test_fib4_small_numbers(self):
        self.assertEqual(fib4(4), 2)
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

    def test_fib4_large_numbers(self):
        self.assertEqual(fib4(10), 55)
        self.assertEqual(fib4(20), 10946)
        self.assertEqual(fib4(30), 267914296)

    def test_fib4_negative_numbers(self):
        self.assertRaises(ValueError, fib4, -1)
        self.assertRaises(ValueError, fib4, -2)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the base cases, small numbers, large numbers, and negative numbers. The `assertRaises` method is used to test for exceptions when passing invalid inputs.