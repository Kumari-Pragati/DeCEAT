You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_59_code import largest_prime_factor

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True

    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_59_code import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(100), 5)
        self.assertEqual(largest_prime_factor(101), 101)
        self.assertEqual(largest_prime_factor(102), 51)
        self.assertEqual(largest_prime_factor(103), 103)
        self.assertEqual(largest_prime_factor(104), 26)
        self.assertEqual(largest_prime_factor(105), 21)
        self.assertEqual(largest_prime_factor(106), 53)
        self.assertEqual(largest_prime_factor(107), 107)
        self.assertEqual(largest_prime_factor(108), 54)
        self.assertEqual(largest_prime_factor(109), 109)
        self.assertEqual(largest_prime_factor(110), 55)
        self.assertEqual(largest_prime_factor(111), 37)
        self.assertEqual(largest_prime_factor(112), 28)
        self.assertEqual(largest_prime_factor(113), 113)
        self.assertEqual(largest_prime_factor(114), 57)
        self.assertEqual(largest_prime_factor(115), 23)
        self.assertEqual(largest_prime_factor(116), 58)
        self.assertEqual(largest_prime_factor(117), 39)
        self.assertEqual(largest_prime_factor(118), 59)
        self.assertEqual(largest_prime_factor(119), 119)
        self.assertEqual(largest_prime_factor(120), 60)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the `largest_prime_factor` function is working correctly. It tests the function with a variety of inputs, including both prime and non-prime numbers.