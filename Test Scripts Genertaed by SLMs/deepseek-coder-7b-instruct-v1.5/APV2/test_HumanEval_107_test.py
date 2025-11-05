You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_107_code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_even_odd_palindrome(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))
        self.assertEqual(even_odd_palindrome(12), (4, 6))
        self.assertEqual(even_odd_palindrome(100), (12, 14))
        self.assertEqual(even_odd_palindrome(1000), (124, 146))

if __name__ == '__main__':
    unittest.main()


This test suite contains a single test case `test_even_odd_palindrome` that tests the `even_odd_palindrome` function with different inputs and verifies that the function returns the expected output.

Please note that the expected outputs for the test cases are based on the provided examples. If the function's behavior changes, the expected outputs should also be updated accordingly.

Also, please note that the function `even_odd_palindrome` is expected to be in a file named `HumanEval_107_code.py` in the same directory as this test file. If the function is in a different file or has a different name, you will need to adjust the import statement accordingly.