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
    return out

 import unittest
from HumanEval_89_code import encrypt

class TestEncryptFunction(unittest.TestCase):

    def test_encrypt_lowercase_simple(self):
        self.assertEqual(encrypt('hi'), 'lm')

    def test_encrypt_lowercase_complex(self):
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')

    def test_encrypt_lowercase_edge(self):
        self.assertEqual(encrypt('gf'), 'kj')

    def test_encrypt_lowercase_edge_case(self):
        self.assertEqual(encrypt('et'), 'ix')

    def test_encrypt_uppercase(self):
        self.assertEqual(encrypt('HELLO'), 'JGNNQP')

    def test_encrypt_non_alphabetic_characters(self):
        self.assertEqual(encrypt('abc123!@#'), 'def456!@#')

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(''), '')

    def test_encrypt_single_character(self):
        self.assertEqual(encrypt('a'), 'e')

    def test_encrypt_single_character_edge_case(self):
        self.assertEqual(encrypt('z'), 'b')

if __name__ == '__main__':
    unittest.main()