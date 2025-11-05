You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_134_code import check_if_last_char_is_a_letter
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(check_if_last_char_is_a_letter(""))

    def test_last_char_is_letter(self):
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))

    def test_last_char_is_not_letter(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))

    def test_last_char_is_letter_with_space(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e "))

    def test_last_char_is_uppercase_letter(self):
        self.assertTrue(check_if_last_char_is_a_letter("apple Pi e"))

    def test_last_char_is_digit(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e1"))

    def test_last_char_is_special_char(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e!"))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios such as an empty string, a string where the last character is a letter, a string where the last character is not a letter, a string where the last character is a letter with a space, a string where the last character is an uppercase letter, a string where the last character is a digit, and a string where the last character is a special character.