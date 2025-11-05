You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    def test_encrypt_single_characters(self):
        self.assertEqual(encrypt('h'), 'j')
        self.assertEqual(encrypt('i'), 'k')
        self.assertEqual(encrypt('a'), 'c')
        self.assertEqual(encrypt('b'), 'd')
        self.assertEqual(encrypt('c'), 'e')
        self.assertEqual(encrypt('d'), 'f')
        self.assertEqual(encrypt('e'), 'g')
        self.assertEqual(encrypt('f'), 'h')
        self.assertEqual(encrypt('g'), 'i')
        self.assertEqual(encrypt('h'), 'j')
        self.assertEqual(encrypt('i'), 'k')
        self.assertEqual(encrypt('j'), 'l')
        self.assertEqual(encrypt('k'), 'm')
        self.assertEqual(encrypt('l'), 'n')
        self.assertEqual(encrypt('m'), 'o')
        self.assertEqual(encrypt('n'), 'p')
        self.assertEqual(encrypt('o'), 'q')
        self.assertEqual(encrypt('p'), 'r')
        self.assertEqual(encrypt('q'), 's')
        self.assertEqual(encrypt('r'), 't')
        self.assertEqual(encrypt('s'), 'u')
        self.assertEqual(encrypt('t'), 'v')
        self.assertEqual(encrypt('u'), 'w')
        self.assertEqual(encrypt('v'), 'x')
        self.assertEqual(encrypt('w'), 'y')
        self.assertEqual(encrypt('x'), 'z')
        self.assertEqual(encrypt('y'), 'a')
        self.assertEqual(encrypt('z'), 'b')

    def test_encrypt_multiple_characters(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')
        self.assertEqual(encrypt('Hello'), 'Jgnnq')
        self.assertEqual(encrypt('Python'), 'R{vjgt')
        self.assertEqual(encrypt('World'), 'C{xqtf')
        self.assertEqual(encrypt('Test'), 'V{gvj')
        self.assertEqual(encrypt('Encrypt'), 'G{kcvgt')
        self.assertEqual(encrypt('Unittest'), 'W{vjgt')

    def test_encrypt_non_alphabet_characters(self):
        self.assertEqual(encrypt('123!@#'), '123!@#')
        self.assertEqual(encrypt('$%^&*'), '$%^&*')
        self.assertEqual(encrypt('123#$%^&*'), '123#$%^&*')

if __name__ == '__main__':
    unittest.main()