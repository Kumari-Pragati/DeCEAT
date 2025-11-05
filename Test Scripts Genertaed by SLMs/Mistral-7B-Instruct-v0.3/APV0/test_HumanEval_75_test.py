Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return False

 Here is a unittest test script for the `is_multiply_prime` function. It includes tests for the edge cases, valid inputs, and invalid inputs.


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_edge_cases(self):
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(2))
        self.assertFalse(is_multiply_prime(4))
        self.assertFalse(is_multiply_prime(7))
        self.assertTrue(is_multiply_prime(30))
        self.assertFalse(is_multiply_prime(101))
        self.assertFalse(is_multiply_prime(120))

    def test_valid_inputs(self):
        for i in range(31, 100):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                self.assertTrue(is_multiply_prime(i))
            else:
                self.assertFalse(is_multiply_prime(i))

    def test_invalid_inputs(self):
        self.assertFalse(is_multiply_prime(-1))
        self.assertFalse(is_multiply_prime(0))
        self.assertFalse(is_multiply_prime(1000))
        self.assertFalse(is_multiply_prime(10000))
        self.assertFalse(is_multiply_prime(float('inf')))
        self.assertFalse(is_multiply_prime(complex(1, 0)))

if __name__ == '__main__':
    unittest.main()


This test script includes three test cases: `test_edge_cases`, `test_valid_inputs`, and `test_invalid_inputs`. The `test_edge_cases` test case checks the edge cases of the function, including the smallest and largest possible inputs. The `test_valid_inputs` test case checks the valid inputs within the given range (31 to 100) that are multiples of 3, 5, or 7. The `test_invalid_inputs` test case checks the invalid inputs, such as negative numbers, zero, large numbers, floating-point numbers, and complex numbers.