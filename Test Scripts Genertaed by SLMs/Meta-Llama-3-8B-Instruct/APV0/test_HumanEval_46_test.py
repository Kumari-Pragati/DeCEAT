user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    return results[-1]assistant

Here is the unittest test script for the `fib4` function:

import unittest
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)
        self.assertEqual(fib4(4), 2)
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

    def test_large_values(self):
        self.assertEqual(fib4(8), 22)
        self.assertEqual(fib4(9), 34)
        self.assertEqual(fib4(10), 54)
        self.assertEqual(fib4(11), 86)
        self.assertEqual(fib4(12), 138)

    def test_edge_cases(self):
        self.assertRaises(ValueError, fib4, -1)
        self.assertRaises(ValueError, fib4, 0.5)

if __name__ == '__main__':
    unittest.main()

This test script includes three test cases:

1. `test_small_values`: Tests the function with small values (0 to 7) to ensure it returns the correct results.
2. `test_large_values`: Tests the function with larger values (8 to 12) to ensure it returns the correct results.
3. `test_edge_cases`: Tests the function with invalid inputs (negative value and non-integer value) to ensure it raises a `ValueError`.

You can run this script directly to execute the tests.