You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
Here is a unittest test suite for the given function:


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
        self.assertFalse(is_palindrome('Abba'))

    def test_whitespace(self):
        self.assertFalse(is_palindrome('A man a plan a canal Panama'))
        self.assertTrue(is_palindrome('A man a plan a canal Panama '))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios, including empty strings, single characters, even and odd length palindromes, non-palindromes, case sensitivity, and whitespace.

Please note that the function `is_palindrome` is assumed to be in a file named `HumanEval_48_code.py` in the same directory as the test file. If the function is in a different location, you would need to adjust the import statement accordingly.

Also, the function does not handle punctuation or special characters, so the test case `test_whitespace` is an example of how to handle whitespace. If you want to test with punctuation or special characters, you would need to add additional test cases.