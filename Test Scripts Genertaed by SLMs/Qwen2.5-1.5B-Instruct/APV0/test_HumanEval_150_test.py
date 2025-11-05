system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_150_code import x_or_y
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x


assistant

import unittest

# Importing the function to be tested
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_x_or_y(self):
        # Test cases for prime numbers
        self.assertEqual(x_or_y(7, 34, 12), 34)
        self.assertEqual(x_or_y(19, 65, 23), 65)

        # Test cases for non-prime numbers
        self.assertEqual(x_or_y(15, 8, 5), 5)
        self.assertEqual(x_or_y(20, 10, 2), 10)

if __name__ == '__main__':
    unittest.main()


This script imports the `unittest` module and the `x_or_y` function from another file named `HumanEval_150_code`. It then defines a class `TestXOrY` that inherits from `unittest.TestCase`, which allows us to write tests for our function. The `test_x_or_y` method contains assertions that check whether the function returns the correct values for given inputs. Finally, it runs all the tests when executed as a standalone script using `unittest.main()`.