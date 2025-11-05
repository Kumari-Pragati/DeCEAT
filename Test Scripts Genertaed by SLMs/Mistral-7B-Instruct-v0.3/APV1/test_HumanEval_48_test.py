You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_48_code import is_palindrome

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

 Here is a comprehensive unittest test suite for the given Python function `is_palindrome`.


import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertTrue(is_palindrome(char))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome('a man a plan a canal Panama'))

    def test_palindrome_with_special_characters(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))
        self.assertFalse(is_palindrome('abac'))
        self.assertFalse(is_palindrome('12345'))
        self.assertFalse(is_palindrome('A1B2C3'))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for empty strings, single characters, palindromes with spaces, palindromes with special characters, and non-palindromes. It covers various edge cases and ensures the `is_palindrome` function behaves as expected.