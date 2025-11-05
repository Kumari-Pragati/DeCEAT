user

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
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else Falseassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_check_if_last_char_is_a_letter(self):
        # Test cases
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e "))
        self.assertFalse(check_if_last_char_is_a_letter(""))
        self.assertFalse(check_if_last_char_is_a_letter("apple"))
        self.assertTrue(check_if_last_char_is_a_letter("apple p i e"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q r"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q r s"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q r s t"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q r s t u"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q r s t u v"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q r s t u v w"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q r s t u v w x"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q r s t u v w x y"))
        self.assertFalse(check_if_last_char_is_a_letter("apple p i e f g h i j k l m n o p q r s t u v w x y z"))

if __name__ == '__main__':
    unittest.main()


This script includes a variety of test cases to ensure the function is working correctly. The test cases cover different scenarios, including strings with and without spaces, and strings with and without alphabetical characters at the end.