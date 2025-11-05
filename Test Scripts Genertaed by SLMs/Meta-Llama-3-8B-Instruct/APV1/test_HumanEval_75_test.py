user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_75_code import is_multiply_prime
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 
    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """

    def is_prime(n):
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return Falseassistant

Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime_true(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(210))
        self.assertTrue(is_multiply_prime(60))
        self.assertTrue(is_multiply_prime(90))

    def test_is_multiply_prime_false(self):
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(2))
        self.assertFalse(is_multiply_prime(3))
        self.assertFalse(is_multiply_prime(4))

    def test_is_multiply_prime_edge_cases(self):
        self.assertTrue(is_multiply_prime(2 * 3 * 5))
        self.assertFalse(is_multiply_prime(100))

    def test_is_multiply_prime_random_numbers(self):
        self.assertTrue(is_multiply_prime(6))
        self.assertFalse(is_multiply_prime(7))
        self.assertTrue(is_multiply_prime(8))
        self.assertFalse(is_multiply_prime(9))

    def test_is_multiply_prime_invalid_input(self):
        with self.assertRaises(TypeError):
            is_multiply_prime("a")
        with self.assertRaises(TypeError):
            is_multiply_prime(None)

if __name__ == '__main__':
    unittest.main()


This test suite covers the following scenarios:

1. `is_multiply_prime_true`: Tests the function with known true cases.
2. `is_multiply_prime_false`: Tests the function with known false cases.
3. `is_multiply_prime_edge_cases`: Tests the function with edge cases.
4. `is_multiply_prime_random_numbers`: Tests the function with random numbers.
5. `is_multiply_prime_invalid_input`: Tests the function with invalid input (non-integer values).

Note that this test suite is not exhaustive, and you may want to add more tests to cover additional scenarios.