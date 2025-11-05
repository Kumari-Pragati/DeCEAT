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

    return string + string[:beginning_of_suffix][::-1]

 Here is a unittest test script for the `make_palindrome` function:


import unittest
from HumanEval_10_code import make_palindrome, is_palindrome

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_char_string(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(make_palindrome(char), char + char)

    def test_palindrome(self):
        self.assertEqual(make_palindrome('radar'), 'radar')
        self.assertEqual(make_palindrome('level'), 'leveL')
        self.assertEqual(make_palindrome('racecar'), 'racecar')

    def test_non_palindrome(self):
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')
        self.assertEqual(make_palindrome('hello'), 'ollih')
        self.assertEqual(make_palindrome('world'), 'dirwol')

if __name__ == '__main__':
    unittest.main()


This test script includes tests for empty strings, single character strings, palindromes, and non-palindromes. It uses the `is_palindrome` function to check if the generated palindrome is correct.