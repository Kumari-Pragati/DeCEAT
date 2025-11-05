user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")

    def test_example2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    def test_single_word(self):
        self.assertEqual(words_in_sentence("Hello"), "Hello")

    def test_multiple_words(self):
        self.assertEqual(words_in_sentence("Hello World"), "Hello World")

    def test_empty_sentence(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_single_word_prime_length(self):
        self.assertEqual(words_in_sentence("a"), "a")

    def test_single_word_non_prime_length(self):
        self.assertEqual(words_in_sentence("ab"), "")

    def test_multiple_words_prime_length(self):
        self.assertEqual(words_in_sentence("Hello World"), "Hello World")

    def test_multiple_words_non_prime_length(self):
        self.assertEqual(words_in_sentence("Hello World ab"), "Hello World")

    def test_sentence_with_spaces(self):
        self.assertEqual(words_in_sentence("   Hello   World   "), "Hello World")

    def test_sentence_with_punctuation(self):
        self.assertEqual(words_in_sentence("Hello, World!"), "Hello")

    def test_sentence_with_numbers(self):
        self.assertEqual(words_in_sentence("Hello 123 World"), "Hello World")

    def test_sentence_with_special_characters(self):
        self.assertEqual(words_in_sentence("Hello @ World"), "Hello World")

if __name__ == '__main__':
    unittest.main()


This test script includes a variety of test cases to ensure the function works correctly in different scenarios. The test cases cover different types of input, including single words, multiple words, empty sentences, sentences with spaces, punctuation, numbers, and special characters.