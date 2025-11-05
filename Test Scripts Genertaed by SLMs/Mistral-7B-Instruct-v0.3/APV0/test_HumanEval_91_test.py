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

 Here is a unittest test script for the `is_bored` function:


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_single_word(self):
        self.assertEqual(is_bored("I am here"), 1)
        self.assertEqual(is_bored("here I am"), 1)

    def test_multiple_sentences(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        self.assertEqual(is_bored("I love this weather. The sky is blue. The sun is shining."), 1)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I hate this weather"), 0)

    def test_punctuation(self):
        self.assertEqual(is_bored("I am here."), 1)
        self.assertEqual(is_bored("I am here?"), 1)
        self.assertEqual(is_bored("I am here!"), 1)
        self.assertEqual(is_bored("I am here. I am here."), 2)
        self.assertEqual(is_bored("I am here. I am here?"), 2)
        self.assertEqual(is_bored("I am here. I am here!"), 2)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I am bored. I am really bored. I am extremely bored."), 3)

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to cover different scenarios, such as an empty string, single words, multiple sentences, punctuation, and multiple boredoms. It tests the function's behavior for various inputs and ensures that the function returns the correct number of boredoms.