system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the `decode_shift` function:


import unittest
from HumanEval_50_code import decode_shift

class TestDecodeShift(unittest.TestCase):

    def test_decode_shift_lowercase(self):
        self.assertEqual(decode_shift("a"), "f")
        self.assertEqual(decode_shift("b"), "g")
        self.assertEqual(decode_shift("c"), "h")
        self.assertEqual(decode_shift("d"), "i")
        self.assertEqual(decode_shift("e"), "j")
        self.assertEqual(decode_shift("f"), "k")
        self.assertEqual(decode_shift("g"), "l")
        self.assertEqual(decode_shift("h"), "m")
        self.assertEqual(decode_shift("i"), "n")
        self.assertEqual(decode_shift("j"), "o")
        self.assertEqual(decode_shift("k"), "p")
        self.assertEqual(decode_shift("l"), "q")
        self.assertEqual(decode_shift("m"), "r")
        self.assertEqual(decode_shift("n"), "s")
        self.assertEqual(decode_shift("o"), "t")
        self.assertEqual(decode_shift("p"), "u")
        self.assertEqual(decode_shift("q"), "v")
        self.assertEqual(decode_shift("r"), "w")
        self.assertEqual(decode_shift("s"), "x")
        self.assertEqual(decode_shift("t"), "y")
        self.assertEqual(decode_shift("u"), "z")
        self.assertEqual(decode_shift("v"), "a")

    def test_decode_shift_uppercase(self):
        self.assertEqual(decode_shift("A"), "F")
        self.assertEqual(decode_shift("B"), "G")
        self.assertEqual(decode_shift("C"), "H")
        self.assertEqual(decode_shift("D"), "I")
        self.assertEqual(decode_shift("E"), "J")
        self.assertEqual(decode_shift("F"), "K")
        self.assertEqual(decode_shift("G"), "L")
        self.assertEqual(decode_shift("H"), "M")
        self.assertEqual(decode_shift("I"), "N")
        self.assertEqual(decode_shift("J"), "O")
        self.assertEqual(decode_shift("K"), "P")
        self.assertEqual(decode_shift("L"), "Q")
        self.assertEqual(decode_shift("M"), "R")
        self.assertEqual(decode_shift("N"), "S")
        self.assertEqual(decode_shift("O"), "T")
        self.assertEqual(decode_shift("P"), "U")
        self.assertEqual(decode_shift("Q"), "V")
        self.assertEqual(decode_shift("R"), "W")
        self.assertEqual(decode_shift("S"), "X")
        self.assertEqual(decode_shift("T"), "Y")
        self.assertEqual(decode_shift("U"), "Z")
        self.assertEqual(decode_shift("V"), "A")

    def test_decode_shift_mixedcase(self):
        self.assertEqual(decode_shift("aBc"), "fGh")
        self.assertEqual(decode_shift("dE"), "iJ")
        self.assertEqual(decode_shift("kL"), "pM")
        self.assertEqual(decode_shift("oP"), "tQ")
        self.assertEqual(decode_shift("sT"), "xU")
        self.assertEqual(decode_shift("vW"), "zA")

    def test_decode_shift_nonalpha(self):
        self.assertEqual(decode_shift("abc123"), "fgh123")
        self.assertEqual(decode_shift(" ABC!@#"), " FGH!@#")
        self.assertEqual(decode_shift("hello world"), "khoor zruog")

if __name__ == '__main__':
    unittest.main()