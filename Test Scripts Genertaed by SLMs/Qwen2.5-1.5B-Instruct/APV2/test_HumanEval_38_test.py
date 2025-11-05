system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


assistant

import unittest

# Provided function
from HumanEval_38_code import decode_cyclic

class TestEncodeCyclic(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(encode_cyclic("abc"), "bac")
        self.assertEqual(encode_cyclic("hello"), "ehllo")
        self.assertEqual(encode_cyclic("world"), "dlorw")

    def test_decode(self):
        self.assertEqual(decode_cyclic("bac"), "abc")
        self.assertEqual(decode_cyclic("ehllo"), "hello")
        self.assertEqual(decode_cyclic("dlorw"), "world")

if __name__ == '__main__':
    unittest.main()


This test suite includes two test methods: `test_encode` and `test_decode`. The first method tests the encoding functionality with various inputs, while the second method checks that decoding correctly reverses the encoding process.