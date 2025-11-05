Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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
        self.assertEqual(vowels_count("b"), 0)

    def test_no_vowels(self):
        self.assertEqual(vowels_count("bcdfgh"), 0)

    def test_vowels_with_y_at_end(self):
        self.assertEqual(vowels_count("abcY"), 2)
        self.assertEqual(vowels_count("XY"), 2)

    def test_vowels_with_y_not_at_end(self):
        self.assertEqual(vowels_count("abcy"), 2)
        self.assertEqual(vowels_count("xyZ"), 1)

    def test_mixed_case_vowels(self):
        self.assertEqual(vowels_count("AbCde"), 2)
        self.assertEqual(vowels_count("aBcDe"), 2)

    def test_multiple_vowels(self):
        self.assertEqual(vowels_count("aeiou"), 5)
        self.assertEqual(vowels_count("AEIOU"), 5)

    def test_no_y_at_end(self):
        self.assertEqual(vowels_count("abcdeY"), 2)
        self.assertEqual(vowels_count("abcde"), 2)

    def test_y_not_at_end(self):
        self.assertEqual(vowels_count("abcdeYz"), 2)
        self.assertEqual(vowels_count("abcde"), 2)

if __name__ == '__main__':
    unittest.main()