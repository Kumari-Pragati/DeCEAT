You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

    def test_single_character(self):
        self.assertEqual(vowels_count("a"), 1)
        self.assertEqual(vowels_count("A"), 1)
        self.assertEqual(vowels_count("b"), 0)

    def test_multiple_characters(self):
        self.assertEqual(vowels_count("abcde"), 2)
        self.assertEqual(vowels_count("ABCDE"), 2)
        self.assertEqual(vowels_count("abCde"), 2)
        self.assertEqual(vowels_count("AbCde"), 2)

    def test_vowels_with_y_at_end(self):
        self.assertEqual(vowels_count("abcdeY"), 3)
        self.assertEqual(vowels_count("ABCdeY"), 3)
        self.assertEqual(vowels_count("abCdeY"), 3)
        self.assertEqual(vowels_count("AbCdeY"), 3)

    def test_vowels_with_y_not_at_end(self):
        self.assertEqual(vowels_count("abcdey"), 2)
        self.assertEqual(vowels_count("ABCdey"), 2)
        self.assertEqual(vowels_count("abCdey"), 2)
        self.assertEqual(vowels_count("AbCdey"), 2)

    def test_no_vowels(self):
        self.assertEqual(vowels_count("xyz"), 0)
        self.assertEqual(vowels_count("XYZ"), 0)
        self.assertEqual(vowels_count("xYz"), 0)
        self.assertEqual(vowels_count("XYZ"), 0)

    def test_mixed_case(self):
        self.assertEqual(vowels_count("aBcDeY"), 4)
        self.assertEqual(vowels_count("AbCdEy"), 4)
        self.assertEqual(vowels_count("aBcDeY"), 4)
        self.assertEqual(vowels_count("AbCdEy"), 4)

if __name__ == '__main__':
    unittest.main()