You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_single_boredom(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I am bored. I have nothing to do. I want to play!"), 3)

    def test_no_boredoms_with_punctuation(self):
        self.assertEqual(is_bored("Hello world!"), 0)

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_boredom_at_start(self):
        self.assertEqual(is_bored("I am starting this test."), 1)

    def test_boredom_at_end(self):
        self.assertEqual(is_bored("This is a test. I am ending it."), 1)

    def test_boredom_in_middle(self):
        self.assertEqual(is_bored("This is a test. I am in the middle. This is the end."), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios, including cases with no boredoms, single boredom, multiple boredoms, boredoms at the start, end, and in the middle of the string, and empty strings.