You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
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

 Here is a complete unittest test suite for the `vowels_count` function:


import unittest
from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_vowels_count_simple(self):
        self.assertEqual(vowels_count("abcde"), 2)
        self.assertEqual(vowels_count("ABCDE"), 2)
        self.assertEqual(vowels_count("aeiou"), 5)
        self.assertEqual(vowels_count("AEIOU"), 5)

    def test_vowels_count_with_y(self):
        self.assertEqual(vowels_count("ACEDY"), 3)
        self.assertEqual(vowels_count("acedy"), 3)
        self.assertEqual(vowels_count("ACED"), 1)
        self.assertEqual(vowels_count("aced"), 1)

    def test_vowels_count_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

    def test_vowels_count_with_special_characters(self):
        self.assertEqual(vowels_count("ae!@#$iou"), 3)
        self.assertEqual(vowels_count("AE!@#$IOU"), 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as simple words, words with 'y' at the end, empty strings, and words with special characters. The test suite uses the `unittest.TestCase` class to define test methods, and the `assertEqual` method to check the expected and actual results.