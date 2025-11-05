You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return True


### Response:
Here is a unittest test script for the given Python function:


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

if __name__ == '__main__':
    unittest.main()


This script creates a test case class `TestPrimeLength` that inherits from `unittest.TestCase`. Inside this class, we define a method `test_prime_length` that tests the `prime_length` function with various inputs. 

The `assertTrue` method is used to check that the function returns `True` when the input string length is a prime number, and `assertFalse` is used to check that the function returns `False` when the input string length is not a prime number.

Finally, the script ends with `if __name__ == '__main__': unittest.main()`, which means that the tests will be run when the script is executed directly.