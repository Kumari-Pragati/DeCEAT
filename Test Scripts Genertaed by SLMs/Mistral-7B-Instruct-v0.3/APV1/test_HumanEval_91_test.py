You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_91_code import is_bored

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """

    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence.startswith('I ') for sentence in sentences if sentence)

 Here is a comprehensive unittest test suite for the given Python function `is_bored`.


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_single_word(self):
        self.assertEqual(is_bored("Hello"), 0)
        self.assertEqual(is_bored("World"), 0)
        self.assertEqual(is_bored("I"), 0)
        self.assertEqual(is_bored("I "), 1)

    def test_multiple_sentences(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        self.assertEqual(is_bored("I'm bored. Let's go out."), 1)
        self.assertEqual(is_bored("I'm not bored. I'm having fun."), 0)
        self.assertEqual(is_bored("I'm bored. I'm bored. I'm bored."), 3)

    def test_punctuation(self):
        self.assertEqual(is_bored("I'm bored!"), 1)
        self.assertEqual(is_bored("I'm bored?"), 1)
        self.assertEqual(is_bored("I'm bored."), 1)
        self.assertEqual(is_bored("I'm bored.."), 1)
        self.assertEqual(is_bored("I'm bored!"), 1)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I'm bored. I'm bored. I'm bored."), 3)
        self.assertEqual(is_bored("I'm bored. I'm not bored. I'm bored again."), 2)

    def test_case_sensitivity(self):
        self.assertEqual(is_bored("I'm bored."), 1)
        self.assertEqual(is_bored("i'm bored."), 1)
        self.assertEqual(is_bored("I'M BORED."), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for edge cases, multiple sentences, multiple boredoms, punctuation, and case sensitivity.