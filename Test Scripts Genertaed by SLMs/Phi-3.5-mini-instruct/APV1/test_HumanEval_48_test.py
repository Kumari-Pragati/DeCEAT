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

 import unittest
from HumanEval_48_code import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome('aba'))

    def test_multiple_characters_palindrome(self):
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))

    def test_case_insensitive_palindrome(self):
        self.assertTrue(is_palindrome('Racecar'))

    def test_case_insensitive_non_palindrome(self):
        self.assertFalse(is_palindrome('Rabbit'))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome('A man a plan a canal Panama'))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome('Able was I ere I saw Elba'))

    def test_palindrome_with_mixed_case(self):
        self.assertTrue(is_palindrome('Madam'))

    def test_palindrome_with_numbers(self):
        self.assertTrue(is_palindrome('1234321'))

    def test_palindrome_with_special_characters(self):
        self.assertTrue(is_palindrome('Abba'))

    def test_palindrome_with_whitespace(self):
        self.assertTrue(is_palindrome('No lemon, no melon'))

if __name__ == '__main__':
    unittest.main()