You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `prime_length` function:


import unittest
from HumanEval_82_code import prime_length

class TestPrimeLength(unittest.TestCase):

    def test_prime_length(self):
        self.assertTrue(prime_length('Hello'))
        self.assertTrue(prime_length('abcdcba'))
        self.assertTrue(prime_length('kittens'))
        self.assertFalse(prime_length('orange'))
        self.assertFalse(prime_length(''))
        self.assertFalse(prime_length('1'))
        self.assertFalse(prime_length('0'))
        self.assertTrue(prime_length('5'))
        self.assertFalse(prime_length('6'))
        self.assertTrue(prime_length('7'))
        self.assertFalse(prime_length('8'))
        self.assertTrue(prime_length('11'))
        self.assertFalse(prime_length('12'))

if __name__ == '__main__':
    unittest.main()


This test suite includes both positive and negative test cases for the `prime_length` function. It covers the base cases (empty string, string of length 1) and prime numbers from 2 to 11.