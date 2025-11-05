You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(105))
        self.assertTrue(is_multiply_prime(189))
        self.assertFalse(is_multiply_prime(10))
        self.assertFalse(is_multiply_prime(15))
        self.assertFalse(is_multiply_prime(20))
        self.assertFalse(is_multiply_prime(21))
        self.assertFalse(is_multiply_prime(22))
        self.assertFalse(is_multiply_prime(25))
        self.assertFalse(is_multiply_prime(35))
        self.assertFalse(is_multiply_prime(40))
        self.assertFalse(is_multiply_prime(42))
        self.assertFalse(is_multiply_prime(45))
        self.assertFalse(is_multiply_prime(50))
        self.assertFalse(is_multiply_prime(55))
        self.assertFalse(is_multiply_prime(60))
        self.assertFalse(is_multiply_prime(66))
        self.assertFalse(is_multiply_prime(70))
        self.assertFalse(is_multiply_prime(77))
        self.assertFalse(is_multiply_prime(80))
        self.assertFalse(is_multiply_prime(85))
        self.assertFalse(is_multiply_prime(90))
        self.assertFalse(is_multiply_prime(99))

if __name__ == '__main__':
    unittest.main()


This script tests the `is_multiply_prime` function with a variety of inputs, including both prime and non-prime numbers. It checks both true and false cases to ensure that the function is working as expected.