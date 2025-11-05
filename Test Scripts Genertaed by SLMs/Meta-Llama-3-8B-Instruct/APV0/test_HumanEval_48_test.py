user

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
        if text[i]!= text[len(text) - 1 - i]:
            return False
    return Trueassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('b'))
        self.assertTrue(is_palindrome('c'))
        # Add more characters as needed

    def test_palindrome(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))
        self.assertTrue(is_palindrome('radar'))
        self.assertTrue(is_palindrome('madam'))
        # Add more palindromes as needed

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('world'))
        # Add more non-palindromes as needed

    def test_spaces(self):
        self.assertFalse(is_palindrome('a b'))
        self.assertFalse(is_palindrome('   '))
        # Add more space-related tests as needed

    def test_punctuation(self):
        self.assertFalse(is_palindrome('a!b'))
        self.assertFalse(is_palindrome('a,b'))
        self.assertFalse(is_palindrome('a?b'))
        # Add more punctuation-related tests as needed

    def test_numbers(self):
        self.assertTrue(is_palindrome('12321'))
        self.assertFalse(is_palindrome('123456'))
        # Add more number-related tests as needed

if __name__ == '__main__':
    unittest.main()


This script includes tests for the following cases:

- An empty string
- A single character
- Palindromes
- Non-palindromes
- Strings with spaces
- Strings with punctuation
- Strings with numbers

You can run this script directly to see the results of the tests.