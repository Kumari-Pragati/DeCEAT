You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_check_if_last_char_is_a_letter(self):
        self.assertEqual(check_if_last_char_is_a_letter("apple pie"), False)
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e"), True)
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e "), False)
        self.assertEqual(check_if_last_char_is_a_letter(""), False)
        self.assertEqual(check_if_last_char_is_a_letter("a"), True)
        self.assertEqual(check_if_last_char_is_a_letter("b"), True)
        self.assertEqual(check_if_last_char_is_a_letter("c"), True)
        self.assertEqual(check_if_last_char_is_a_letter("d"), True)
        self.assertEqual(check_if_last_char_is_a_letter("e"), True)
        self.assertEqual(check_if_last_char_is_a_letter("f"), True)
        self.assertEqual(check_if_last_char_is_a_letter("g"), True)
        self.assertEqual(check_if_last_char_is_a_letter("h"), True)
        self.assertEqual(check_if_last_char_is_a_letter("i"), True)
        self.assertEqual(check_if_last_char_is_a_letter("j"), True)
        self.assertEqual(check_if_last_char_is_a_letter("k"), True)
        self.assertEqual(check_if_last_char_is_a_letter("l"), True)
        self.assertEqual(check_if_last_char_is_a_letter("m"), True)
        self.assertEqual(check_if_last_char_is_a_letter("n"), True)
        self.assertEqual(check_if_last_char_is_a_letter("o"), True)
        self.assertEqual(check_if_last_char_is_a_letter("p"), True)
        self.assertEqual(check_if_last_char_is_a_letter("q"), True)
        self.assertEqual(check_if_last_char_is_a_letter("r"), True)
        self.assertEqual(check_if_last_char_is_a_letter("s"), True)
        self.assertEqual(check_if_last_char_is_a_letter("t"), True)
        self.assertEqual(check_if_last_char_is_a_letter("u"), True)
        self.assertEqual(check_if_last_char_is_a_letter("v"), True)
        self.assertEqual(check_if_last_char_is_a_letter("w"), True)
        self.assertEqual(check_if_last_char_is_a_letter("x"), True)
        self.assertEqual(check_if_last_char_is_a_letter("y"), True)
        self.assertEqual(check_if_last_char_is_a_letter("z"), True)
        self.assertEqual(check_if_last_char_is_a_letter(" "), False)
        self.assertEqual(check_if_last_char_is_a_letter("1"), False)
        self.assertEqual(check_if_last_char_is_a_letter("2"), False)
        self.assertEqual(check_if_last_char_is_a_letter("3"), False)
        self.assertEqual(check_if_last_char_is_a_letter("4"), False)
        self.assertEqual(check_if_last_char_is_a_letter("5"), False)
        self.assertEqual(check_if_last_char_is_a_letter("6"), False)
        self.assertEqual(check_if_last_char_is_a_letter("7"), False)
        self.assertEqual(check_if_last_char_is_a_letter("8"), False)
        self