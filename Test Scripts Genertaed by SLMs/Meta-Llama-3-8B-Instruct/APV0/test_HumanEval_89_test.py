user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_89_code import encrypt
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """

    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c) + 4) % 26]
        else:
            out += c
    return outassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_89_code import encrypt

class TestEncryptFunction(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')
        self.assertEqual(encrypt('abcdefghijklmnopqrstuvwxyz'),'stuvwxyzabcde')
        self.assertEqual(encrypt('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'),'stuvwxyzabcdeabcdefghijklmnopqrstuvwxyz')
        self.assertEqual(encrypt(''), '')
        self.assertEqual(encrypt('abc'), 'efg')
        self.assertEqual(encrypt('xyz'), 'abc')

    def test_non_alphabetic_characters(self):
        self.assertEqual(encrypt('hello world'), 'ixmmp xpsme')

    def test_punctuation(self):
        self.assertEqual(encrypt('Hello, World!'), 'Khoor, Zruog!')

    def test_uppercase_letters(self):
        self.assertEqual(encrypt('HELLO'), 'KHOOR')

    def test_mixed_case(self):
        self.assertEqual(encrypt('HeLlO'), 'KHoOr')

    def test_spaces(self):
        self.assertEqual(encrypt('Hello World'), 'Khoor Zruog')

    def test_newline(self):
        self.assertEqual(encrypt('Hello\nWorld'), 'Khoor\nZruog')

    def test_tabs(self):
        self.assertEqual(encrypt('Hello\tWorld'), 'Khoor\tZruog')

if __name__ == '__main__':
    unittest.main()


This test script includes a variety of test cases to ensure the function is working correctly. It tests the function with different inputs, including strings with and without non-alphabetic characters, punctuation, uppercase letters, mixed case, spaces, newlines, and tabs.