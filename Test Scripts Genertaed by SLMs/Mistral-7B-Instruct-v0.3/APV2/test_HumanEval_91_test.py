You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `is_bored` function:


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
        self.assertEqual(is_bored("I am bored. I am very bored. I am extremely bored."), 3)
        self.assertEqual(is_bored("I'm bored. I'm very bored. I'm extremely bored."), 3)
        self.assertEqual(is_bored("I'm bored! I'm very bored! I'm extremely bored!"), 3)
        self.assertEqual(is_bored("I'm bored.\nI'm very bored.\nI'm extremely bored."), 3)

    def test_punctuation(self):
        self.assertEqual(is_bored("I, am, bored."), 1)
        self.assertEqual(is_bored("I am, bored."), 1)
        self.assertEqual(is_bored("I am bored!"), 1)
        self.assertEqual(is_bored("I am bored?"), 1)
        self.assertEqual(is_bored("I am bored?!"), 1)
        self.assertEqual(is_bored("I am bored.\nI am very bored.\nI am extremely bored."), 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty string, single words, multiple sentences, and sentences with punctuation. It uses the `unittest.TestCase` class to define test methods and the `assertEqual` method to verify the expected output.