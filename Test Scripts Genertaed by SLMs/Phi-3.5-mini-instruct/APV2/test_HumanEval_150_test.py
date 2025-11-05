You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_number_one(self):
        self.assertEqual(x_or_y(1, 34, 12), 12)

    def test_even_number(self):
        self.assertEqual(x_or_y(4, 34, 12), 12)

    def test_zero(self):
        self.assertEqual(x_or_y(0, 34, 12), 12)

    def test_negative_number(self):
        self.assertEqual(x_or_y(-7, 34, 12), 12)

    def test_non_integer_number(self):
        self.assertEqual(x_or_y(3.14, 34, 12), 12)

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `x_or_y` function:

1. Testing with a prime number (7) should return `x` (34).
2. Testing with a non-prime number (15) should return `y` (5).
3. Testing with the number 1 should return `y` (12).
4. Testing with an even number (4) should return `y` (12).
5. Testing with zero should return `y` (12).
6. Testing with a negative number (-7) should return `y` (12).
7. Testing with a non-integer number (3.14) should return `y` (12).

Each test case uses `self.assertEqual` to verify that the `x_or_y` function returns the expected result. Running this test suite will execute all the tests and report any failures.