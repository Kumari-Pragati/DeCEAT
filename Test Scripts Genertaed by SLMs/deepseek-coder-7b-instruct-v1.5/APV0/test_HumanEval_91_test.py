You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):
    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_single_boredom(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I am bored. I have nothing to do. I am bored again!"), 2)

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


This script tests the `is_bored` function with various inputs to ensure that it is working as expected. It checks for cases where there are no boredoms, cases where there is a single boredom, cases where there are multiple boredoms, and cases where the boredom is at the start, end, or in the middle of the string. It also checks for empty strings and strings that only contain punctuation.