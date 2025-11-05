You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return out

 Here is a complete unittest test suite for the provided `encrypt` function:


import unittest
from HumanEval_89_code import encrypt

class TestEncrypt(unittest.TestCase):

    def test_encrypt_single_letter(self):
        self.assertEqual(encrypt('a'), 'd')
        self.assertEqual(encrypt('b'), 'e')
        self.assertEqual(encrypt('z'), 'c')

    def test_encrypt_multiple_letters(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_encrypt_mixed_case(self):
        self.assertEqual(encrypt('HeLlO'), 'MnOpQrStUv')
        self.assertEqual(encrypt('WoRlD'), 'XyZaEbF')
        self.assertEqual(encrypt('12345'), '12345')

    def test_encrypt_special_characters(self):
        self.assertEqual(encrypt('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '~@#$%^&*()_+-=[]{}|;:\"><,>.?/')
        self.assertEqual(encrypt('ABC!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 'DEF~@#$%^&*()_+-=[]{}|;:\"><,>.?/')

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as single letters, multiple letters, mixed case, and special characters. The test cases are designed to ensure that the `encrypt` function behaves as expected for the given problem statement.