You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `is_multiply_prime`. The test cases cover a range of numbers that are multiplications of 3 prime numbers and some that are not.


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime_true(self):
        test_cases = [6, 12, 18, 20, 30, 36, 42, 48, 54, 60, 72, 90]
        for test_case in test_cases:
            self.assertTrue(is_multiply_prime(test_case))

    def test_is_multiply_prime_false(self):
        test_cases = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 33, 34, 35, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 49, 51, 52, 53, 55, 56, 57, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        for test_case in test_cases:
            self.assertFalse(is_multiply_prime(test_case))

if __name__ == '__main__':
    unittest.main()


This test suite includes two test methods: `test_is_multiply_prime_true` and `test_is_multiply_prime_false`. The first method tests the function with numbers that are multiplications of 3 prime numbers, and the second method tests the function with numbers that are not multiplications of 3 prime numbers.