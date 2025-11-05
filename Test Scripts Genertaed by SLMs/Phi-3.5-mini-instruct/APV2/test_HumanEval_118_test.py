You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    def test_get_closest_vowel_with_vowel_between_consonants(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")

    def test_get_closest_vowel_with_vowel_at_end(self):
        self.assertEqual(get_closest_vowel("FULL"), "U")

    def test_get_closest_vowel_with_no_vowel_between_consonants(self):
        self.assertEqual(get_closest_vowel("quick"), "")

    def test_get_closest_vowel_with_only_two_letters(self):
        self.assertEqual(get_closest_vowel("ab"), "")

    def test_get_closest_vowel_with_vowel_at_start(self):
        self.assertEqual(get_closest_vowel("a"), "")

    def test_get_closest_vowel_with_vowel_at_end_and_consonant_before(self):
        self.assertEqual(get_closest_vowel("burt"), "u")

    def test_get_closest_vowel_with_consonant_at_start_and_end(self):
        self.assertEqual(get_closest_vowel("brt"), "")

    def test_get_closest_vowel_with_multiple_vowels(self):
        self.assertEqual(get_closest_vowel("queue"), "")

    def test_get_closest_vowel_with_no_vowels(self):
        self.assertEqual(get_closest_vowel("rhythm"), "")

    def test_get_closest_vowel_with_mixed_case(self):
        self.assertEqual(get_closest_vowel("YoU"), "U")

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `get_closest_vowel` function, including words with vowels between consonants, vowels at the end of the word, words with only two letters, vowels at the start of the word, words with multiple vowels, and mixed-case words. Each test case checks for the expected output using the `assertEqual` method from the `unittest` framework.