You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_10_code import make_palindrome

class TestMakePalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_character(self):
        self.assertEqual(make_palindrome('c'), 'c')

    def test_single_word(self):
        self.assertEqual(make_palindrome('cat'), 'catac')

    def test_already_palindrome(self):
        self.assertEqual(make_palindrome('level'), 'level')

    def test_multiple_characters(self):
        self.assertEqual(make_palindrome('race'), 'racecar')

    def test_multiple_words(self):
        self.assertEqual(make_palindrome('abcd'), 'abcddcba')

    def test_non_palindrome_single_char(self):
        self.assertEqual(make_palindrome('a'), 'a')

    def test_non_palindrome_multiple_chars(self):
        self.assertEqual(make_palindrome('ab'), 'aba')

    def test_non_palindrome_multiple_words(self):
        self.assertEqual(make_palindrome('abcde'), 'abcdeedcba')

    def test_special_characters(self):
        self.assertEqual(make_palindrome('a!b@c#'), 'a!b@c#cba#@b!a')

    def test_case_insensitivity(self):
        self.assertEqual(make_palindrome('Race'), 'Racecar')

    def test_empty_string_case_insensitivity(self):
        self.assertEqual(make_palindrome(''), '')

if __name__ == '__main__':
    unittest.main()