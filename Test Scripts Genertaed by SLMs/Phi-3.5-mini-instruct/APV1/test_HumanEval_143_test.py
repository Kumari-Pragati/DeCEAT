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

 import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_single_letter_word(self):
        self.assertEqual(words_in_sentence("a"), "a")

    def test_two_letter_word(self):
        self.assertEqual(words_in_sentence("is"), "is")

    def test_multiple_words(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    def test_empty_string(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_no_prime_length_words(self):
        self.assertEqual(words_in_sentence("this is a test"), "this is a test")

    def test_prime_length_words(self):
        self.assertEqual(words_in_sentence("this is a prime"), "is a")

    def test_mixed_length_words(self):
        self.assertEqual(words_in_sentence("this is a long word with 7 letters"), "is a")

    def test_single_space_sentence(self):
        self.assertEqual(words_in_sentence("word"), "word")

    def test_multiple_spaces_sentence(self):
        self.assertEqual(words_in_sentence("word  word"), "word")

    def test_sentence_with_numbers(self):
        self.assertEqual(words_in_sentence("123 is a number"), "is")

    def test_sentence_with_special_characters(self):
        self.assertEqual(words_in_sentence("!@# is a special"), "is a")

if __name__ == '__main__':
    unittest.main()