system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Importing the function we want to test
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_single_sentence(self):
        self.assertEqual(is_bored("I am happy."), 1)

    def test_multiple_sentences(self):
        self.assertEqual(is_bored("I am happy. I am excited!"), 2)

    def test_complex_sentence(self):
        self.assertEqual(is_bored("I am feeling bored today. However, I am not really bored."),
                         1)

    def test_no_I_start(self):
        self.assertEqual(is_bored("This is an interesting day."),
                         0)

    def test_mixed_punctuation(self):
        self.assertEqual(is_bored("I'm having fun. What about you?"),
                         1)

if __name__ == '__main__':
    unittest.main()


This script includes all necessary imports at the beginning, tests various scenarios as described in the docstring, and ends with `unittest.main()` to run the tests when executed directly.