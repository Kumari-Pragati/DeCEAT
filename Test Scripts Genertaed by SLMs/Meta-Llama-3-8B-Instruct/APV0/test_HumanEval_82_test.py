user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return Trueassistant

Here is the unittest test script for the `prime_length` function:

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
        self.assertTrue(prime_length('abc'))
        self.assertTrue(prime_length('abcdef'))
        self.assertFalse(prime_length('abcdefg'))

if __name__ == '__main__':
    unittest.main()

This test script includes a variety of test cases to ensure that the `prime_length` function is working correctly. The test cases cover the following scenarios:

* Positive test cases: `prime_length('Hello')`, `prime_length('abcdcba')`, `prime_length('kittens')`, and `prime_length('abc')` should all return `True`.
* Negative test cases: `prime_length('orange')`, `prime_length('')`, `prime_length('a')`, and `prime_length('abcdefg')` should all return `False`.
* Edge cases: `prime_length('')` and `prime_length('a')` are tested to ensure that the function correctly handles strings of length 0 and 1, respectively.

You can run this test script directly by saving it to a file (e.g., `test_prime_length.py`) and executing it using Python (e.g., `python test_prime_length.py`).