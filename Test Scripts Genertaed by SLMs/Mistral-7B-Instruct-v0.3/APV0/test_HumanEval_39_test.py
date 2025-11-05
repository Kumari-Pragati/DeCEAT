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
            return f[-1]

 Here is a unittest test script for the `prime_fib` function. The script includes test cases for various inputs and asserts that the function returns the expected output.


import unittest
from HumanEval_39_code import prime_fib

class TestPrimeFib(unittest.TestCase):
    def test_prime_fib_1(self):
        self.assertEqual(prime_fib(1), 2)

    def test_prime_fib_2(self):
        self.assertEqual(prime_fib(2), 3)

    def test_prime_fib_3(self):
        self.assertEqual(prime_fib(3), 5)

    def test_prime_fib_4(self):
        self.assertEqual(prime_fib(4), 13)

    def test_prime_fib_5(self):
        self.assertEqual(prime_fib(5), 89)

    def test_prime_fib_6(self):
        self.assertEqual(prime_fib(6), 233)

    def test_prime_fib_7(self):
        self.assertEqual(prime_fib(7), 1597)

    def test_prime_fib_8(self):
        self.assertEqual(prime_fib(8), 28657)

    def test_prime_fib_9(self):
        self.assertEqual(prime_fib(9), 515329)

    def test_prime_fib_10(self):
        self.assertEqual(prime_fib(10), 13584029)

if __name__ == '__main__':
    unittest.main()


This script includes test cases for inputs ranging from 1 to 10, but you can add more test cases as needed to cover a wider range of inputs or edge cases.