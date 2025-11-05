Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_38_code import decode_cyclic
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups, each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group, unless the group has fewer than 3 elements.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function.
    Returns decoded string.
    """
    return encode_cyclic(encode_cyclic(s))

 import unittest
from HumanEval_38_code import encode_cyclic

class TestCyclicEncoding(unittest.TestCase):

    def test_encode_cyclic_empty_string(self):
        self.assertEqual(encode_cyclic(''), '')

    def test_encode_cyclic_single_character(self):
        self.assertEqual(encode_cyclic('a'), 'a')

    def test_encode_cyclic_two_characters(self):
        self.assertEqual(encode_cyclic('ab'), 'ba')

    def test_encode_cyclic_three_characters(self):
        self.assertEqual(encode_cyclic('abc'), 'bca')

    def test_encode_cyclic_four_characters(self):
        self.assertEqual(encode_cyclic('abcd'), 'bcda')

    def test_encode_cyclic_fifteen_characters(self):
        self.assertEqual(encode_cyclic('abcdefghijklmno'), 'bcdfehgijkmnola')

    def test_decode_cyclic_empty_string(self):
        self.assertEqual(decode_cyclic(''), '')

    def test_decode_cyclic_single_character(self):
        self.assertEqual(decode_cyclic('a'), 'a')

    def test_decode_cyclic_two_characters(self):
        self.assertEqual(decode_cyclic('ba'), 'ab')

    def test_decode_cyclic_three_characters(self):
        self.assertEqual(decode_cyclic('bca'), 'abc')

    def test_decode_cyclic_four_characters(self):
        self.assertEqual(decode_cyclic('bcda'), 'abcd')

    def test_decode_cyclic_fifteen_characters(self):
        self.assertEqual(decode_cyclic('bcdfehgijkmnola'), 'abcdefghijklmno')

if __name__ == '__main__':
    unittest.main()