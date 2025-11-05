system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return " ".join(new_lst)assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")

    def test_example2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    def test_single_word(self):
        self.assertEqual(words_in_sentence("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(words_in_sentence("apple banana orange"), "apple banana")

    def test_empty_sentence(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_sentence_with_no_prime_length_words(self):
        self.assertEqual(words_in_sentence("a b c d e f"), "a b c d e f")

    def test_sentence_with_all_prime_length_words(self):
        self.assertEqual(words_in_sentence("2 3 5 7 11"), "2 3 5 7 11")

    def test_sentence_with_mixed_length_words(self):
        self.assertEqual(words_in_sentence("hello world 123"), "hello world")

    def test_sentence_with_repeated_words(self):
        self.assertEqual(words_in_sentence("hello hello world"), "hello world")

    def test_sentence_with_spaces(self):
        self.assertEqual(words_in_sentence("   hello   world   "), "hello world")

if __name__ == '__main__':
    unittest.main()