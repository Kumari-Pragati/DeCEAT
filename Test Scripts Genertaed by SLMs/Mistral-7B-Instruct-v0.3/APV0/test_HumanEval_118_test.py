Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `get_closest_vowel` function:


import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    def test_get_closest_vowel(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")
        self.assertEqual(get_closest_Vowel("FULL"), "U")
        self.assertEqual(get_closest_vowel("quick"), "")
        self.assertEqual(get_closest_vowel("ab"), "")
        self.assertEqual(get_closest_vowel("example"), "a")
        self.assertEqual(get_closest_vowel("education"), "a")
        self.assertEqual(get_closest_vowel("banana"), "a")
        self.assertEqual(get_closest_vowel("consonant"), "")
        self.assertEqual(get_closest_vowel("vowel"), "")
        self.assertEqual(get_closest_vowel("aeiou"), "")
        self.assertEqual(get_closest_vowel("AEIOU"), "")
        self.assertEqual(get_closest_vowel("123"), "")
        self.assertEqual(get_closest_vowel("abc"), "")
        self.assertEqual(get_closest_vowel("Hello, World!"), "")

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases for the `get_closest_vowel` function, ensuring that it works correctly for different inputs. The test cases cover a variety of scenarios, including words with and without vowels between two consonants, words with only vowels, words with only consonants, and words with special characters.