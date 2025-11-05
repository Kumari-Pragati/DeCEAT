system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_86_code import anti_shuffle
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string is a string where all words (separated by space)
    are replaced by a new word where all the characters are arranged in
    ascending order based on ASCII value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


assistant

import unittest

# Provided function
from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(anti_shuffle(""), "")

    def test_single_word(self):
        self.assertEqual(anti_shuffle("Hi"), "Hi")

    def test_multiple_words(self):
        self.assertEqual(anti_shuffle("hello world!"), "ehllo !worl dl!")

    def test_with_numbers(self):
        self.assertEqual(anti_shuffle("The quick brown fox 123 jumps over the lazy dog"), 
                         "The eikc uqkn brwno xof 321 jmps ov erht yzg dgo")

    def test_with_special_characters(self):
        self.assertEqual(anti_shuffle("This is a test!"), "hsiT si a ett!")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios including empty strings, single words, multiple words, numbers, and special characters. It uses the `assertEqual` method to check if the output matches the expected result.