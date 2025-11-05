You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_words_in_sentence(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")
        self.assertEqual(words_in_sentence("a"), "a")
        self.assertEqual(words_in_sentence("This is a test of the emergency broadcast system"), "is a of the")
        self.assertEqual(words_in_sentence("The quick brown fox jumps over the lazy dog"), "quick brown jumps over lazy")
        self.assertEqual(words_in_sentence(""), "")

if __name__ == '__main__':
    unittest.main()


This script tests the `words_in_sentence` function with a variety of inputs, including single-word sentences, sentences with words of length 1 and 2, and sentences with words of lengths that are prime numbers. It also tests the function with an empty sentence.

Please note that the function `words_in_sentence` is assumed to be in a file named `HumanEval_143_code.py` in the same directory as this unittest script. If the function is in a different location, you will need to adjust the import statement accordingly.

Also, the function `words_in_sentence` is not optimized for large inputs. If you want to test it with larger inputs, you may need to optimize the function or add additional tests.