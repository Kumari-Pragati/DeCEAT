You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_single_boredom(self):
        self.assertEqual(is_bored("The sky is blue. I love the stars!"), 1)

    def test_multiple_boredom(self):
        self.assertEqual(is_bored("The sky is blue. I love the stars! I enjoy the night sky."), 2)

    def test_no_sentence_delimiters(self):
        self.assertEqual(is_bored("I am happy"), 1)

    def test_sentence_with_multiple_delimiters(self):
        self.assertEqual(is_bored("I am happy. I am excited! I am thrilled."), 3)

    def test_no_boredom_with_sentence_starting_with_i(self):
        self.assertEqual(is_bored("I am not bored"), 1)

    def test_no_boredom_with_sentence_not_starting_with_i(self):
        self.assertEqual(is_bored("The sky is blue. I am not bored"), 1)

    def test_empty_sentence(self):
        self.assertEqual(is_bored("I am. I am."), 2)

    def test_sentence_with_leading_whitespace(self):
        self.assertEqual(is_bored(" I am bored."), 1)

if __name__ == '__main__':
    unittest.main()