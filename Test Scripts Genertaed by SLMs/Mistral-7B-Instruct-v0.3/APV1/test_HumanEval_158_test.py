You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_158_code import find_max

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    Examples:
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    """
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]

 Here is a comprehensive unittest test suite for the given Python function `find_max`. The test suite includes various test cases to cover different scenarios and edge cases.


import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_max([]))

    def test_single_word(self):
        self.assertEqual(find_max(["word"]), "word")

    def test_single_word_with_duplicates(self):
        self.assertEqual(find_max(["aa", "aa"]), "aa")

    def test_multiple_words_with_unique_chars(self):
        self.assertEqual(find_max(["one", "two", "three"]), "one")

    def test_multiple_words_with_same_unique_chars(self):
        self.assertEqual(find_max(["enam", "name"]), "enam")

    def test_multiple_words_with_different_unique_chars(self):
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_multiple_words_with_same_unique_chars_lexicographical_order(self):
        self.assertEqual(find_max(["enam", "name"]), "enam")

    def test_multiple_words_with_same_unique_chars_different_lengths(self):
        self.assertEqual(find_max(["enam", "nam"]), "enam")

    def test_multiple_words_with_same_unique_chars_different_lengths_lexicographical_order(self):
        self.assertEqual(find_max(["nam", "enam"]), "nam")

if __name__ == '__main__':
    unittest.main()


This test suite covers the following scenarios:

1. Empty list
2. Single word
3. Multiple words with unique characters
4. Multiple words with the same unique characters
5. Multiple words with different unique characters
6. Multiple words with the same unique characters in lexicographical order
7. Multiple words with the same unique characters, different lengths
8. Multiple words with the same unique characters, different lengths in lexicographical order