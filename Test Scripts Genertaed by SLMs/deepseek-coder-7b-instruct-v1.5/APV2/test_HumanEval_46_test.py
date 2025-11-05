You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):
    def test_fib4_small_numbers(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)

    def test_fib4_large_numbers(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

    def test_fib4_negative_numbers(self):
        with self.assertRaises(IndexError):
            fib4(-1)

    def test_fib4_non_integer_input(self):
        with self.assertRaises(TypeError):
            fib4(1.5)

    def test_fib4_large_numbers(self):
        self.assertEqual(fib4(10), 144)
        self.assertEqual(fib4(20), 16796)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for small numbers, large numbers, negative numbers, and non-integer inputs. It checks that the function returns the correct values for the given inputs and that it raises the correct exceptions for invalid inputs.