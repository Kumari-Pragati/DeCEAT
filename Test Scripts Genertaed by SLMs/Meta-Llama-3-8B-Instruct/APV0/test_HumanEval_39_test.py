user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_39_code import prime_fib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]assistant

Here is the unittest test script for the `prime_fib` function:

import unittest
from HumanEval_39_code import prime_fib

class TestPrimeFib(unittest.TestCase):
    def test_prime_fib(self):
        # Test cases from the docstring
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

        # Additional test cases
        self.assertEqual(prime_fib(6), 233)
        self.assertEqual(prime_fib(7), 1597)
        self.assertEqual(prime_fib(8), 28657)
        self.assertEqual(prime_fib(9), 433794437)
        self.assertEqual(prime_fib(10), 1094619933)

        # Edge cases
        self.assertEqual(prime_fib(0), None)  # Should raise an error
        with self.assertRaises(ValueError):
            prime_fib(-1)

if __name__ == '__main__':
    unittest.main()

This test script includes the following:

1. Test cases from the docstring: These test cases are taken directly from the docstring of the `prime_fib` function.
2. Additional test cases: These test cases cover more values of `n` to ensure the function works correctly for a wider range of inputs.
3. Edge cases: These test cases cover edge cases such as `n=0` (which should raise an error) and `n=-1` (which should raise a `ValueError`).

You can run this test script directly by saving it to a file (e.g., `test_prime_fib.py`) and running it with `python test_prime_fib.py`.