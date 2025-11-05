You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python functions:


import unittest
from HumanEval_10_code import make_palindrome, is_palindrome

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_char_string(self):
        self.assertEqual(make_palindrome('c'), 'c')

    def test_palindrome_string(self):
        self.assertEqual(make_palindrome('catac'), 'catac')

    def test_non_palindrome_string(self):
        self.assertEqual(make_palindrome('cat'), 'catac')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertFalse(is_palindrome('hello'))

if __name__ == '__main__':
    unittest.main()


This script tests the `make_palindrome` function with different types of inputs, including empty strings, single character strings, palindrome strings, and non-palindrome strings. It also tests the `is_palindrome` function with both palindrome and non-palindrome strings.