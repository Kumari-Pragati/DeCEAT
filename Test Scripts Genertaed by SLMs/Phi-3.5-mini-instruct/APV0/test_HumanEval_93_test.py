Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_93_code import encode
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])

 import unittest
from HumanEval_93_code import encode

class TestEncodeFunction(unittest.TestCase):

    def test_swapcase(self):
        self.assertEqual(encode('test'), 'TGST')

    def test_vowel_replacement(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

    def test_no_change_for_non_vowels(self):
        self.assertEqual(encode('Hello World'), 'hFLLO WORLd')

    def test_empty_string(self):
        self.assertEqual(encode(''), '')

    def test_single_character(self):
        self.assertEqual(encode('a'), 'c')

    def test_special_characters(self):
        self.assertEqual(encode('!@#$%^&*()'), '!@#$%^&*()')

    def test_uppercase_vowels(self):
        self.assertEqual(encode('AEIOU'), 'CEIOU')

    def test_lowercase_vowels(self):
        self.assertEqual(encode('aeiou'), 'cgkqu')

    def test_mixed_case_vowels(self):
        self.assertEqual(encode('AeIoU'), 'CgKQu')

if __name__ == '__main__':
    unittest.main()