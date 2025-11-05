system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_89_code import encrypt

class TestEncryptFunction(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')
        self.assertEqual(encrypt('hello'), 'khoor')
        self.assertEqual(encrypt('world'), 'xpsme')
        self.assertEqual(encrypt('python'), 'ubvqrp')
        self.assertEqual(encrypt('unittest'), 'vyhgnqf')

    def test_non_alphabet_characters(self):
        self.assertEqual(encrypt('hello123'), 'khoor123')
        self.assertEqual(encrypt('!@#$%^&*()'), '!@#$%^&*()')

    def test_empty_string(self):
        self.assertEqual(encrypt(''), '')

    def test_single_character(self):
        self.assertEqual(encrypt('a'), 'e')
        self.assertEqual(encrypt('z'), 'c')

    def test_multiple_spaces(self):
        self.assertEqual(encrypt('   hello   '),'  khoor   ')

    def test_punctuation(self):
        self.assertEqual(encrypt('Hello, World!'), 'Khoor, Xpsme!')

    def test_uppercase_letters(self):
        self.assertEqual(encrypt('HELLO'), 'KHOOR')
        self.assertEqual(encrypt('WORLD'), 'XPSME')

if __name__ == '__main__':
    unittest.main()