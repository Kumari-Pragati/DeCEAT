user

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
    return sum(sentence.startswith('I ') for sentence in sentences if sentence)assistant

Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("This is a test"), 0)
        self.assertEqual(is_bored("I love Python, but I hate unittest"), 1)

    def test_one_boredom(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        self.assertEqual(is_bored("I am bored. I want to sleep."), 2)
        self.assertEqual(is_bored("I love this weather. I hate that weather"), 2)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I love Python. I hate unittest. I love coding"), 3)
        self.assertEqual(is_bored("I am bored. I want to sleep. I love to code"), 3)
        self.assertEqual(is_bored("I love this weather. I hate that weather. I love to code"), 3)

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_no_sentences(self):
        self.assertEqual(is_bored("   "), 0)

    def test_non_sentence_input(self):
        self.assertEqual(is_bored("I love Python"), 1)
        self.assertEqual(is_bored("I hate unittest"), 1)
        self.assertEqual(is_bored("I love coding"), 1)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including:

* No boredoms
* One boredom
* Multiple boredoms
* Empty string
* No sentences
* Non-sentence input

Each test case checks the output of the `is_bored` function against the expected result.