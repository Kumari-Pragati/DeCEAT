Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `check_if_last_char_is_a_letter` function:


import unittest
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(check_if_last_char_is_a_letter(""))

    def test_single_word(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple"))
        self.assertFalse(check_if_last_char_is_a_letter("pie"))

    def test_multiple_words(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e "))

    def test_special_characters(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple#"))
        self.assertFalse(check_if_last_char_is_a_letter("apple%"))
        self.assertFalse(check_if_last_char_is_a_letter("apple_"))

    def test_numbers(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple1"))
        self.assertFalse(check_if_last_char_is_a_letter("apple2"))
        self.assertFalse(check_if_last_char_is_a_letter("apple3"))

    def test_uppercase_letters(self):
        self.assertTrue(check_if_last_char_is_a_letter("APPLE"))
        self.assertTrue(check_if_last_char_is_a_letter("PIE"))

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to cover different scenarios, such as empty strings, single words, multiple words, special characters, numbers, and uppercase letters. It uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.