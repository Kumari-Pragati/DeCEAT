You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


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
        self.assertFalse(is_palindrome('a b'))

if __name__ == '__main__':
    unittest.main()


This script creates a unittest.TestCase subclass with several test methods that test different scenarios. Each method calls the `is_palindrome` function with a specific input and asserts that the result matches the expected result.

Please note that the `HumanEval_48_code` module and the `is_palindrome` function should be defined in a separate file named `HumanEval_48_code.py` in the same directory. If they are not, you will need to replace `from HumanEval_48_code import is_palindrome` with the actual definition of the `is_palindrome` function.