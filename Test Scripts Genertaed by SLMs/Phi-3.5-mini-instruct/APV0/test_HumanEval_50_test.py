Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_50_code import decode_shift
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input a string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

 import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift(self):
        self.assertEqual(encode_shift('hello'), 'mjqqt')
        self.assertEqual(encode_shift('world'), 'btwqi')
        self.assertEqual(encode_shift('python'), 'udymts')
        self.assertEqual(encode_shift(''), '')  # Test empty string
        self.assertEqual(encode_shift('a'), 'f')  # Test single character

    def test_decode_shift(self):
        self.assertEqual(decode_shift('mjqqt'), 'hello')
        self.assertEqual(decode_shift('btwqi'), 'world')
        self.assertEqual(decode_shift('udymts'), 'python')
        self.assertEqual(decode_shift(''), '')  # Test empty string
        self.assertEqual(decode_shift('f'), 'a')  # Test single character

    def test_encode_shift_with_uppercase(self):
        self.assertEqual(encode_shift('Hello'), 'Mjqqt')
        self.assertEqual(encode_shift('WORLD'), 'BTWQI')
        self.assertEqual(encode_shift('PYTHON'), 'UDYMTS')

    def test_decode_shift_with_uppercase(self):
        self.assertEqual(decode_shift('Mjqqt'), 'Hello')
        self.assertEqual(decode_shift('BTWQI'), 'WORLD')
        self.assertEqual(decode_shift('UDYMTS'), 'PYTHON')

    def test_encode_shift_with_non_alphabet_characters(self):
        self.assertEqual(encode_shift('abc123!@#'), 'fgi673!@#')

    def test_decode_shift_with_non_alphabet_characters(self):
        self.assertEqual(decode_shift('fgi673!@#'), 'abc123!@#')

    def test_encode_shift_with_mixed_cases(self):
        self.assertEqual(encode_shift('HelloWorld'), 'MjqqtBtwqi')
        self.assertEqual(encode_shift('Python3'), 'Udymts3')

    def test_decode_shift_with_mixed_cases(self):
        self.assertEqual(decode_shift('MjqqtBtwqi'), 'HelloWorld')
        self.assertEqual(decode_shift('Udymts3'), 'Python3')

if __name__ == '__main__':
    unittest.main()