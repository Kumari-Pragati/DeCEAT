You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    def test_get_closest_vowel_with_vowel_between_consonants(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")

    def test_get_closest_vowel_with_vowel_at_start(self):
        self.assertEqual(get_closest_vowel("FULL"), "U")

    def test_get_closest_vowel_with_no_vowel_between_consonants(self):
        self.assertEqual(get_closest_vowel("quick"), "")

    def test_get_closest_vowel_with_only_two_letters(self):
        self.assertEqual(get_closest_vowel("ab"), "")

    def test_get_closest_vowel_with_vowel_at_end(self):
        self.assertEqual(get_closest_vowel("bac"), "a")

    def test_get_closest_vowel_with_vowel_at_both_ends(self):
        self.assertEqual(get_closest_vowel("aba"), "")

    def test_get_closest_vowel_with_consonants_only(self):
        self.assertEqual(get_closest_vowel("xyz"), "")

    def test_get_closest_vowel_with_uppercase_vowel(self):
        self.assertEqual(get_closest_vowel("Yogurt"), "u")

    def test_get_closest_vowel_with_uppercase_consonants(self):
        self.assertEqual(get_closest_vowel("FULL"), "U")

    def test_get_closest_vowel_with_mixed_case(self):
        self.assertEqual(get_closest_vowel("qUick"), "u")

if __name__ == '__main__':
    unittest.main()