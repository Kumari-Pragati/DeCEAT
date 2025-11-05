You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_lowercase_vowels(self):
        self.assertEqual(vowels_count("abcde"), 2)

    def test_uppercase_vowels(self):
        self.assertEqual(vowels_count("ACEDY"), 3)

    def test_no_vowels(self):
        self.assertEqual(vowels_count("bcdfghjklmnpqrstvwxyz"), 0)

    def test_y_as_vowel(self):
        self.assertEqual(vowels_count("y"), 1)

    def test_y_at_end(self):
        self.assertEqual(vowels_count("happy"), 2)

    def test_y_as_vowel_uppercase(self):
        self.assertEqual(vowels_count("Y"), 1)

    def test_y_at_end_uppercase(self):
        self.assertEqual(vowels_count("HAPPY"), 2)

    def test_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

if __name__ == '__main__':
    unittest.main()


This script tests the function `vowels_count` with various inputs to ensure it's working as expected. It checks for lowercase and uppercase vowels, words with no vowels, words ending in 'y' or 'Y', and empty strings.