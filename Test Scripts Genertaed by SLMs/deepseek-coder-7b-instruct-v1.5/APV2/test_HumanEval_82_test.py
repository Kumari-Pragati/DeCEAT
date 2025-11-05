You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_82_code import prime_length
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_82_code import prime_length

class TestPrimeLength(unittest.TestCase):
    def test_prime_length(self):
        self.assertTrue(prime_length('Hello'))
        self.assertTrue(prime_length('abcdcba'))
        self.assertTrue(prime_length('kittens'))
        self.assertFalse(prime_length('orange'))
        self.assertFalse(prime_length(''))
        self.assertFalse(prime_length('a'))
        self.assertFalse(prime_length('abcdefgh'))
        self.assertTrue(prime_length('abcdefg'))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various string lengths, including prime and non-prime lengths. It checks both the cases where the string length is prime and where it is not. It also checks the cases where the string length is 0 and 1, which are not prime numbers.