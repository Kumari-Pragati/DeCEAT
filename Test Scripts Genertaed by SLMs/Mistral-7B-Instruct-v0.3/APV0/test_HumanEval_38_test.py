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

 Here is a unittest test script for the `encode_cyclic` and `decode_cyclic` functions:


import unittest
from HumanEval_38_code import encode_cyclic, decode_cyclic

class TestCyclicEncoding(unittest.TestCase):

    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic("abc"), "abc")
        self.assertEqual(encode_cyclic("a"), "a")
        self.assertEqual(encode_cyclic("abcdef"), "abcddeef")
        self.assertEqual(encode_cyclic("abcdefg"), "abcddefg")
        self.assertEqual(encode_cyclic("abcdefghij"), "abcddefghij")
        self.assertEqual(encode_cyclic("abcdefghijkl"), "abcddefghijkl")
        self.assertEqual(encode_cyclic("abcdefghijklm"), "abcddefghijklm")
        self.assertEqual(encode_cyclic("abcdefghijklmnop"), "abcddefghijklmnop")

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic("abc"), "abc")
        self.assertEqual(decode_cyclic("a"), "a")
        self.assertEqual(decode_cyclic("abcddeef"), "abcdef")
        self.assertEqual(decode_cyclic("abcddefg"), "abcdefg")
        self.assertEqual(decode_cyclic("abcddefg"), "abcdefg")
        self.assertEqual(decode_cyclic("abcddefghij"), "abcdefghij")
        self.assertEqual(decode_cyclic("abcddefghijkl"), "abcdefghijkl")
        self.assertEqual(decode_cyclic("abcddefghijklm"), "abcdefghijklm")
        self.assertEqual(decode_cyclic("abcddefghijklmnop"), "abcdefghijklmnop")

if __name__ == '__main__':
    unittest.main()


This test script includes two test cases: `test_encode_cyclic` and `test_decode_cyclic`. The `test_encode_cyclic` tests the `encode_cyclic` function with various inputs, and the `test_decode_cyclic` tests the `decode_cyclic` function with the same outputs from `encode_cyclic`. The test script uses the `unittest` module to run the tests.