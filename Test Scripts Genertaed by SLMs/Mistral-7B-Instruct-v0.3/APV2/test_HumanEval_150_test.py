You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `x_or_y` function:


import unittest
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_x_or_y_with_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)
        self.assertEqual(x_or_y(13, 45, 10), 45)
        self.assertEqual(x_or_y(17, 23, 15), 23)

    def test_x_or_y_with_non_prime_number(self):
        self.assertEqual(x_or_y(4, 12, 34), 34)
        self.assertEqual(x_or_y(6, 5, 12), 5)
        self.assertEqual(x_or_y(10, 8, 15), 8)

if __name__ == '__main__':
    unittest.main()


This test suite includes two test cases: `test_x_or_y_with_prime_number` and `test_x_or_y_with_non_prime_number`. Each test case checks the function's behavior for prime and non-prime numbers, respectively. The test suite uses the `assertEqual` method to verify the expected output for each test case.