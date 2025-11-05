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

 Here is a unittest test script for the `vowels_count` function:


import unittest
from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_vowels_count(self):
        self.assertEqual(vowels_count("abcde"), 2)
        self.assertEqual(vowels_count("ACEDY"), 3)
        self.assertEqual(vowels_count("apple"), 2)
        self.assertEqual(vowels_count("banana"), 3)
        self.assertEqual(vowels_count("Python"), 2)
        self.assertEqual(vowels_count("yellow"), 2)
        self.assertEqual(vowels_count(""), 0)
        self.assertEqual(vowels_count("Hello, World!"), 3)
        self.assertEqual(vowels_count("Hey, there! How's it going?"), 5)

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases for the `vowels_count` function, covering different scenarios such as uppercase and lowercase letters, words with multiple vowels, words with the letter 'y' at the end, and empty strings. The test cases are defined in the `test_vowels_count` method, which is a subclass of `unittest.TestCase`. The test script will run all the test cases when executed directly.