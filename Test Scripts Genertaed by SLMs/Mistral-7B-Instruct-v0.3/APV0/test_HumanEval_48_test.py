Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the provided function `is_palindrome`. The script includes test cases for various inputs to ensure the function works as expected.


import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertTrue(is_palindrome(char))

    def test_palindrome(self):
        test_cases = [
            ('aba', True),
            ('level', True),
            ('racecar', True),
            ('radar', True),
            ('rotor', True),
            ('deified', True),
        ]
        for test_case in test_cases:
            self.assertEqual(is_palindrome(test_case[0]), test_case[1])

    def test_non_palindrome(self):
        test_cases = [
            ('zbcd', False),
            ('hello', False),
            ('world', False),
            ('python', False),
            ('javascript', False),
        ]
        for test_case in test_cases:
            self.assertFalse(is_palindrome(test_case[0]), test_case[1])

if __name__ == '__main__':
    unittest.main()


This script includes test cases for empty strings, single characters, palindromes, and non-palindromes. It uses the `unittest.TestCase` class to define test methods, and the `unittest.main()` function to run the tests.