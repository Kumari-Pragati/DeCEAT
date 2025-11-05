You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_64_code import vowels_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
FIX = """
Add more test cases.
"""


def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels

 import unittest
from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

    def test_single_letter(self):
        self.assertEqual(vowels_count("a"), 1)
        self.assertEqual(vowels_count("A"), 1)

    def test_no_vowels(self):
        self.assertEqual(vowels_count("bcdfg"), 0)

    def test_vowels_in_middle(self):
        self.assertEqual(vowels_count("abc"), 1)
        self.assertEqual(vowels_count("xyz"), 0)

    def test_vowels_at_end_with_y(self):
        self.assertEqual(vowels_count("abcY"), 2)
        self.assertEqual(vowels_count("xyzY"), 1)

    def test_vowels_at_end_without_y(self):
        self.assertEqual(vowels_count("abc"), 1)
        self.assertEqual(vowels_count("xyz"), 0)

    def test_multiple_vowels(self):
        self.assertEqual(vowels_count("aeiou"), 5)
        self.assertEqual(vowels_count("AEIOU"), 5)

    def test_uppercase_y_at_end(self):
        self.assertEqual(vowels_count("aeiOY"), 3)
        self.assertEqual(vowels_count("AEIOY"), 5)

    def test_mixed_case(self):
        self.assertEqual(vowels_count("aBcDeF"), 3)
        self.assertEqual(vowels_count("AbCdEf"), 3)

    def test_no_y_at_end(self):
        self.assertEqual(vowels_count("abcdef"), 2)
        self.assertEqual(vowels_count("ABCDEF"), 2)

    def test_special_characters(self):
        self.assertEqual(vowels_count("!@#$%^&*"), 0)

    def test_whitespace(self):
        self.assertEqual(vowels_count("   "), 0)

    def test_numbers(self):
        self.assertEqual(vowels_count("12345"), 0)

    def test_mixed_content(self):
        self.assertEqual(vowels_count("a1b2c3d4e5"), 3)
        self.assertEqual(vowels_count("A1B2C3D4E5"), 3)

if __name__ == '__main__':
    unittest.main()