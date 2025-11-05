You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return False


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(210))
        self.assertTrue(is_multiply_prime(105))
        self.assertFalse(is_multiply_prime(40))
        self.assertFalse(is_multiply_prime(100))
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(0))
        self.assertFalse(is_multiply_prime(-1))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various inputs, including some edge cases (like 0, 1, -1, and numbers greater than 100). The tests check that the function returns True when the input is the multiplication of 3 prime numbers, and False otherwise.

Please note that the function `is_multiply_prime` is not efficient for large inputs, as it checks all possible combinations of 3 prime numbers. A more efficient solution would be to generate all prime numbers up to 100 first, and then check all combinations of 3 of these.