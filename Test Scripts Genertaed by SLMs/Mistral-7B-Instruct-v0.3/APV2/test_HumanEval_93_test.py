You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the provided `encode` function:


import unittest
from HumanEval_93_code import encode

class TestEncodeFunction(unittest.TestCase):

    def test_encode_single_word(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('Test'), 'tGST')
        self.assertEqual(encode('TeSt'), 'tGsT')

    def test_encode_multiple_words(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')
        self.assertEqual(encode('Hello World'), 'hLlO wRLD')
        self.assertEqual(encode('Good Morning'), 'gDd Noon')

    def test_edge_cases(self):
        self.assertEqual(encode('A'), 'C')
        self.assertEqual(encode('E'), 'G')
        self.assertEqual(encode('I'), 'K')
        self.assertEqual(encode('O'), 'Q')
        self.assertEqual(encode('U'), 'W')
        self.assertEqual(encode('Y'), 'Z')
        self.assertEqual(encode('Ae'), 'Cg')
        self.assertEqual(encode('Ei'), 'Gh')
        self.assertEqual(encode('Io'), 'Qp')
        self.assertEqual(encode('Uo'), 'Ws')
        self.assertEqual(encode('AeI'), 'CgH')
        self.assertEqual(encode('EiO'), 'GhQ')
        self.assertEqual(encode('AeIO'), 'CgHQ')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for single words, multiple words, edge cases with only one vowel, and edge cases with multiple vowels. The test suite uses the `unittest.TestCase` class to define test methods, and the `assertEqual` method to verify that the expected and actual outputs match.