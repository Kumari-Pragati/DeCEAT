You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_75_code import is_multiply_prime
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 
    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """

    def is_prime(n):
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        # Test cases where the number is the multiplication of 3 prime numbers
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(105))
        self.assertTrue(is_multiply_prime(210))

        # Test cases where the number is not the multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(15))
        self.assertFalse(is_multiply_prime(20))
        self.assertFalse(is_multiply_prime(100))

        # Test cases where the number is less than 100
        self.assertFalse(is_multiply_prime(5))
        self.assertFalse(is_multiply_prime(11))
        self.assertFalse(is_multiply_prime(17))

        # Test cases where the number is greater than 100
        self.assertFalse(is_multiply_prime(105))
        self.assertFalse(is_multiply_prime(200))
        self.assertFalse(is_multiply_prime(300))

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the `is_multiply_prime` function is working correctly. It tests both positive and negative scenarios, including cases where the input is a multiplication of 3 prime numbers and cases where it is not. It also tests cases where the input is less than 100 and greater than 100.