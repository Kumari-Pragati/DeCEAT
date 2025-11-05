You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('abba'))

    def test_odd_length_palindrome(self):
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))

    def test_case_sensitivity(self):
        self.assertFalse(is_palindrome('AbBa'))

    def test_whitespace(self):
        self.assertFalse(is_palindrome('a b'))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for empty strings, single characters, even-length palindromes, odd-length palindromes, non-palindromes, case sensitivity, and whitespace.