user

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
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])assistant

Here is a unittest test script for the `decode_shift` function:

Python
import unittest
from HumanEval_50_code import decode_shift

class TestDecodeShift(unittest.TestCase):

    def test_decode_shift(self):
        # Test case 1: Shifted lowercase letters
        self.assertEqual(decode_shift("fghijklmnopqrstuvwxyzabc"), "abc")
        
        # Test case 2: Shifted uppercase letters
        self.assertEqual(decode_shift("FGHIJKLMNOPQRSTUVWXYZABC"), "ABC")
        
        # Test case 3: Shifted digits
        self.assertEqual(decode_shift("0123456789"), "0123456789")
        
        # Test case 4: Shifted special characters
        self.assertEqual(decode_shift("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"), "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
        
        # Test case 5: Shifted empty string
        self.assertEqual(decode_shift(""), "")

        # Test case 6: Shifted string with spaces
        self.assertEqual(decode_shift("   "), "   ")

        # Test case 7: Shifted string with punctuation
        self.assertEqual(decode_shift(".,;?!"), ",.!?")

        # Test case 8: Shifted string with mixed characters
        self.assertEqual(decode_shift("Hello, World!"), "Hello, World!")

if __name__ == '__main__':
    unittest.main()


This script tests the `decode_shift` function with various test cases, including:

- Shifted lowercase and uppercase letters
- Digits
- Special characters
- Empty string
- String with spaces
- String with punctuation
- String with mixed characters

Each test case checks if the output of the `decode_shift` function matches the expected output.