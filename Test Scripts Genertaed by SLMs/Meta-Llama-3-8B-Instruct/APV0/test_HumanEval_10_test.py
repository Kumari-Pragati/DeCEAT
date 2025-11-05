user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_10_code import make_palindrome
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]assistant

Here is the unittest test script for the `make_palindrome` function:

import unittest
from HumanEval_10_code import make_palindrome

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(make_palindrome(""), "")

    def test_single_character(self):
        self.assertEqual(make_palindrome("a"), "a" + "a"[::-1])

    def test_short_palindrome(self):
        self.assertEqual(make_palindrome("cata"), "catac")

    def test_long_palindrome(self):
        self.assertEqual(make_palindrome("abcdef"), "abcdefedcba")

    def test_non_palindrome(self):
        self.assertEqual(make_palindrome("hello"), "hello" + "hello"[::-1])

    def test_long_non_palindrome(self):
        self.assertEqual(make_palindrome("abcdefghijklmnopqrstuvwxyz"), "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz"[::-1])

    def test_edge_cases(self):
        self.assertEqual(make_palindrome("a" * 100), "a" * 100 + "a" * 100[::-1])
        self.assertEqual(make_palindrome("a" * 1000), "a" * 1000 + "a" * 1000[::-1])

if __name__ == '__main__':
    unittest.main()

This test script covers various scenarios, including:

* An empty string
* A single-character string
* A short palindrome
* A long palindrome
* A non-palindrome
* Long non-palindromes
* Edge cases with repeated characters

Each test method uses the `assertEqual` method to verify that the output of the `make_palindrome` function matches the expected result.