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

 Here is a unittest test script for the provided function:


import unittest
from HumanEval_93_code import encode

class TestEncodeFunction(unittest.TestCase):

    def test_encode_single_word(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('Test'), 'tGST')
        self.assertEqual(encode('Test123'), 'tGST123')

    def test_encode_multiple_words(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')
        self.assertEqual(encode('Hello World'), 'hLlO wRLD')
        self.assertEqual(encode('Hello123 World456'), 'hLlO123 wRLD456')

    def test_encode_sentence_with_punctuation(self):
        self.assertEqual(encode('This is a . message, with ! a ? question.'), 'tHKS KS C . MGSSCGG, WIH T A ? QUESTION.')
        self.assertEqual(encode('Hello, World!'), 'hLlO, wRLD!')

    def test_encode_empty_string(self):
        self.assertEqual(encode(''), '')

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as single words, multiple words, sentences with punctuation, and an empty string. It uses the unittest's `assertEqual` method to verify the expected and actual outputs.