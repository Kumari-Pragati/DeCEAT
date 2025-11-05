You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_89_code import encrypt

class TestEncrypt(unittest.TestCase):

    def test_lowercase(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_uppercase(self):
        self.assertEqual(encrypt('HI'), 'LM')
        self.assertEqual(encrypt('ASDFGHJKL'), 'EWHJKLMNO')
        self.assertEqual(encrypt('GF'), 'KJ')
        self.assertEqual(encrypt('ET'), 'IX')

    def test_special_characters(self):
        self.assertEqual(encrypt('!@#$%^&*()'), '!@#$%^&*()')
        self.assertEqual(encrypt('1234567890'), '1234567890')
        self.assertEqual(encrypt(' '), ' ')

if __name__ == '__main__':
    unittest.main()


This script includes three test cases:

1. `test_lowercase`: Tests the function with lowercase letters.
2. `test_uppercase`: Tests the function with uppercase letters.
3. `test_special_characters`: Tests the function with special characters and spaces.

Each test case checks if the function's output matches the expected output. If the function's output is different from the expected output, the test case will fail.

Please note that you need to have the function `encrypt` defined in the file `HumanEval_89_code.py`. If the function is defined in a different file, you need to replace `HumanEval_89_code` with the correct file name.