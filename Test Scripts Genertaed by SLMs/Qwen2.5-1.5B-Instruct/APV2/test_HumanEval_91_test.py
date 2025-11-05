system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function to be tested
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_is_bored(self):
        self.assertEqual(is_bored(""), 0)
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        self.assertEqual(is_bored("I am bored. I need some entertainment."), 1)
        self.assertEqual(is_bored("What's up? How are you? I'm fine."), 0)
        self.assertEqual(is_bored("I have no idea what you're talking about. Can't you tell me?"), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the `is_bored` function works correctly under various conditions as described in the docstring.