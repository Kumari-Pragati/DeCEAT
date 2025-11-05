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
    return sum(sentence.startswith('I ') for sentence in sentences if sentence)assistant

Here is the unittest test script for the `is_bored` function:

import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):
    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_one_boredom(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I am bored. I love this weather. The sun is shining"), 2)

    def test_no_sentences(self):
        self.assertEqual(is_bored(""), 0)

    def test_empty_sentence(self):
        self.assertEqual(is_bored("I am bored.."), 1)

    def test_no_boredoms_after_punctuation(self):
        self.assertEqual(is_bored("The sun is shining. I love this weather!"), 1)

    def test_boredoms_across_multiple_lines(self):
        self.assertEqual(is_bored("I am bored.\nI love this weather.\nThe sun is shining"), 2)

if __name__ == '__main__':
    unittest.main()

This test script covers a variety of scenarios to ensure the `is_bored` function is working correctly. It tests:

1. No boredoms in the input string
2. One boredom in the input string
3. Multiple boredoms in the input string
4. No sentences in the input string (i.e., an empty string)
5. An empty sentence (i.e., a sentence with no words)
6. Boredoms that occur after punctuation (e.g., a period, question mark, or exclamation mark)
7. Boredoms that span multiple lines

Each test case uses the `assertEqual` method to verify that the output of the `is_bored` function matches the expected result.