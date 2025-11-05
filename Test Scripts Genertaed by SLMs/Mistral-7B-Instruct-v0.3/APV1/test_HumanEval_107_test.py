You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_107_code import even_odd_palindrome

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        if i % 2 == 1 and is_palindrome(i):
            odd_palindrome_count += 1
        elif i % 2 == 0 and is_palindrome(i):
            even_palindrome_count += 1

    return (even_palindrome_count, odd_palindrome_count)

 Here is a comprehensive unittest test suite for the given Python function `even_odd_palindrome`.


import unittest
from HumanEval_107_code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_even_odd_palindrome(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))
        self.assertEqual(even_odd_palindrome(5), (1, 2))
        self.assertEqual(even_odd_palindrome(7), (1, 3))
        self.assertEqual(even_odd_palindrome(10), (3, 5))
        self.assertEqual(even_odd_palindrome(15), (4, 7))
        self.assertEqual(even_odd_palindrome(20), (5, 8))
        self.assertEqual(even_odd_palindrome(30), (7, 12))
        self.assertEqual(even_odd_palindrome(50), (10, 18))
        self.assertEqual(even_odd_palindrome(100), (20, 34))
        self.assertEqual(even_odd_palindrome(1000), (154, 296))

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for various input values, ranging from 3 to 1000, and checks if the function returns the correct number of even and odd integer palindromes. The test cases are designed to cover a wide range of input values to ensure the function works correctly for different scenarios.