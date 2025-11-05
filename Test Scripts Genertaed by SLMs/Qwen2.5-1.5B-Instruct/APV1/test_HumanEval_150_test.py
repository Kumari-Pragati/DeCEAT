system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

# Importing the function we want to test
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)
    
    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_single_input(self):
        self.assertEqual(x_or_y(1, 9, 6), 6)

    def test_zero_input(self):
        self.assertEqual(x_or_y(0, 10, 2), 2)

    def test_negative_input(self):
        self.assertEqual(x_or_y(-3, -10, -5), -5)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class named `TestXOrY`. It includes several test methods that cover different scenarios as described in the docstring of the `x_or_y` function. Each method checks whether the function returns the expected result for specific inputs. The `unittest.main()` call at the end runs all the defined tests when this script is executed directly.