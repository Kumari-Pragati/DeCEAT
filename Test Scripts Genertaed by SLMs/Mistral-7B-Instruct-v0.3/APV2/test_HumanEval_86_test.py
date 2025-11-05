You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `anti_shuffle` function:


import unittest
from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(anti_shuffle(''), '')

    def test_single_word(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello'), 'Hello')

    def test_multiple_words(self):
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')
        self.assertEqual(anti_shuffle('Good morning, beautiful day!'), 'Gdoood mornnig, beutiful day!')
        self.assertEqual(anti_shuffle('The quick brown fox jumps over the lazy dog.'), 'The qqqq iiiiikk  brownnn ffffox  jjumps  oooover  ttttheee  llllaazy  ddddogg.' )

    def test_punctuation(self):
        self.assertEqual(anti_shuffle('Hello, World!'), 'Hello !!!Wdlor')
        self.assertEqual(anti_shuffle('It\'s a beautiful day.'), 'It\'\'s a bbbbeeeeautiful ddaayy.')
        self.assertEqual(anti_shuffle("Don't worry, be happy!"), "Don\'\'t wworry, bbeee  hhappy!")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty string, single words, multiple words, and strings with punctuation. It covers various edge cases and ensures that the function behaves as expected.