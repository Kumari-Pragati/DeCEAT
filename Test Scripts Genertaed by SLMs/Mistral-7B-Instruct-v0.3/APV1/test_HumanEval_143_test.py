You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_143_code import words_in_sentence

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word) % i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)

 Here is a comprehensive unittest test suite for the `words_in_sentence` function:


import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_empty_sentence(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_single_word_sentence(self):
        self.assertEqual(words_in_sentence("one"), "one")
        self.assertEqual(words_in_sentence("two"), "")
        self.assertEqual(words_in_sentence("three"), "three")
        self.assertEqual(words_in_sentence("four"), "")
        self.assertEqual(words_in_sentence("five"), "five")

    def test_short_sentence(self):
        self.assertEqual(words_in_sentence("short sentence"), "sentence")
        self.assertEqual(words_in_sentence("short words"), "words")
        self.assertEqual(words_in_sentence("words short"), "short")
        self.assertEqual(words_in_sentence("short and short"), "and")
        self.assertEqual(words_in_sentence("short words short"), "")

    def test_long_sentence(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")
        self.assertEqual(words_in_sentence("I am learning Python programming"), "learning Python programming")
        self.assertEqual(words_in_sentence("The quick brown fox jumps over the lazy dog"), "brown fox jumps over the lazy dog")
        self.assertEqual(words_in_sentence("How now brown cow"), "now brown cow")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for edge cases, such as an empty sentence, single-word sentences, and sentences with words of various lengths. It also includes tests for sentences with multiple words that have prime lengths, as well as sentences with words that have non-prime lengths. The test suite uses the `unittest.TestCase` class to create test cases and the `assertEqual` method to check the expected and actual outputs.