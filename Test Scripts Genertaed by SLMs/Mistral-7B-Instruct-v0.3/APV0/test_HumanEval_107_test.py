Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the given function `even_odd_palindrome`. The test script checks the function with various inputs and verifies the correctness of the output.


import unittest
from HumanEval_107_code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_even_odd_palindrome(self):
        test_cases = [
            (3, (1, 2)),
            (5, (1, 3)),
            (7, (1, 3)),
            (10, (3, 5)),
            (12, (4, 6)),
            (15, (5, 7)),
            (20, (7, 9)),
            (100, (29, 51)),
            (1000, (199, 499))
        ]

        for n, expected in test_cases:
            with self.subTest(n=n):
                result = even_odd_palindrome(n)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


This test script defines a test case class `TestEvenOddPalindrome` with a single test method `test_even_odd_palindrome`. The test method contains a list of test cases with their expected outputs. For each test case, the function is called with the given input, and the result is compared to the expected output using the `assertEqual` method.

To run the test script, simply save it as a .py file and execute it using the command `python filename.py`. The test script will run all the test cases and report the results.