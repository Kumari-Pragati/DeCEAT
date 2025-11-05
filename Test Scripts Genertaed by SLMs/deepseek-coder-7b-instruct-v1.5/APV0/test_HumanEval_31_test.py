You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_31_code import is_prime
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_31_code import is_prime

class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()


This script creates a unittest test case for the `is_prime` function. It tests the function with a variety of inputs, including both prime and non-prime numbers. The `unittest.TestCase` class provides a number of assertion methods that can be used to check whether the function's output matches the expected output. In this case, the `assertFalse` and `assertTrue` methods are used to check whether the function returns `False` or `True` for a given input.

To run this script, you would need to have the `is_prime` function defined in a file named `HumanEval_31_code.py` in the same directory as the test script.