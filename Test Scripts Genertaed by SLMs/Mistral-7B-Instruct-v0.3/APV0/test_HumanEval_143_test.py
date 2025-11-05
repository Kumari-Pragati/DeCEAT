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
    return " ".join(new_lst)

 Here is a unittest test script for the `words_in_sentence` function:


import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_words_in_sentence(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")
        self.assertEqual(words_in_sentence("abc"), "")
        self.assertEqual(words_in_sentence("a"), "a")
        self.assertEqual(words_in_sentence("ab"), "ab")
        self.assertEqual(words_in_sentence("aa"), "a")
        self.assertEqual(words_in_sentence("aabb"), "")
        self.assertEqual(words_in_sentence("aaa"), "a")
        self.assertEqual(words_in_sentence("This is a test This is another test"), "is another")
        self.assertEqual(words_in_sentence(""), "")
        self.assertEqual(words_in_sentence("This is a test This is another test This is yet another test"), "is another")

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to cover different scenarios, including edge cases, and ensures that the function behaves as expected. The test cases cover sentences with different lengths, sentences containing only one word, sentences with words of different lengths, and sentences with multiple occurrences of the same word.