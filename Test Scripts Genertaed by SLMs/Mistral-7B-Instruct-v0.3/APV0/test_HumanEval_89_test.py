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

 Here is a unittest test script for the provided `encrypt` function:


import unittest
from HumanEval_89_code import encrypt

class TestEncryptFunction(unittest.TestCase):
    def test_encrypt_simple_strings(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(''), '')

    def test_encrypt_mixed_case_strings(self):
        self.assertEqual(encrypt('HeLlO'), 'MnKzO')
        self.assertEqual(encrypt('AeSsDfGhJkLnOp'), 'TvQrIuWxYz')

    def test_encrypt_special_characters(self):
        self.assertEqual(encrypt('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '}{_`"|;:'\'<>,.?/zaqwertyuiopasdfghjklxzcvbnm')

    def test_encrypt_numbers(self):
        self.assertEqual(encrypt('12345'), '12345')
        self.assertEqual(encrypt('123456'), '123456')

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to cover different scenarios, such as empty strings, mixed case strings, special characters, and numbers. The test cases use the `assertEqual` method to compare the expected output with the actual output produced by the `encrypt` function.