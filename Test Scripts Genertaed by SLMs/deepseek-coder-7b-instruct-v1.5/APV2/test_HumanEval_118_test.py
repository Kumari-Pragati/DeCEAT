You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_118_code import get_closest_vowel
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if (word[i + 1] not in vowels) and (word[i - 1] not in vowels):
                return word[i]
    return ""


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    def test_get_closest_vowel(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")
        self.assertEqual(get_closest_vowel("FULL"), "U")
        self.assertEqual(get_closest_vowel("quick"), "")
        self.assertEqual(get_closest_vowel("ab"), "")
        self.assertEqual(get_closest_vowel(""), "")
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("b"), "")
        self.assertEqual(get_closest_vowel("aeiou"), "")
        self.assertEqual(get_closest_vowel("bcdfg"), "")
        self.assertEqual(get_closest_vowel("aeiouy"), "y")
        self.assertEqual(get_closest_vowel("bcdfgv"), "v")
        self.assertEqual(get_closest_vowel("bcdfgV"), "V")
        self.assertEqual(get_closest_vowel("bcdfgA"), "A")
        self.assertEqual(get_closest_vowel("bcdfgI"), "I")
        self.assertEqual(get_closest_vowel("bcdfgO"), "O")
        self.assertEqual(get_closest_vowel("bcdfgU"), "U")
        self.assertEqual(get_closest_vowel("bcdfgE"), "E")

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the `get_closest_vowel` function behaves as expected. It tests with different scenarios including empty strings, single characters, words with vowels only, words with vowels at the beginning and end, and words with vowels in between consonants.