You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `anti_shuffle`. The test suite includes various test cases to ensure the function works correctly for different inputs.


import unittest
from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(anti_shuffle(''), '')

    def test_single_word(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello'), 'Hello')
        self.assertEqual(anti_shuffle('World'), 'World')

    def test_multiple_words(self):
        self.assertEqual(anti_shuffle('Hi there'), 'Hi there')
        self.assertEqual(anti_shuffle('hello world'), 'ehllo World')
        self.assertEqual(anti_shuffle('Hello World'), 'Hello World')
        self.assertEqual(anti_shuffle('World Hello'), 'World Hello')

    def test_punctuation(self):
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')
        self.assertEqual(anti_shuffle('Hello, World!!!'), 'Hello , !!!Wdlor')
        self.assertEqual(anti_shuffle('Hello. World!!!'), 'Hello . !!!Wdlor')
        self.assertEqual(anti_shuffle('Hello; World!!!'), 'Hello ; !!!Wdlor')

    def test_special_characters(self):
        self.assertEqual(anti_shuffle('Hello@World!!!'), 'Hello@ !!!Wdlor')
        self.assertEqual(anti_shuffle('Hello#World!!!'), 'Hello# !!!Wdlor')
        self.assertEqual(anti_shuffle('Hello$World!!!'), 'Hello$ !!!Wdlor')
        self.assertEqual(anti_shuffle('Hello%World!!!'), 'Hello% !!!Wdlor')

    def test_numbers(self):
        self.assertEqual(anti_shuffle('Hello123World!!!'), 'Hello123 !!!Wdlor')
        self.assertEqual(anti_shuffle('Hello123World456!!!'), 'Hello123 World456 !!!')
        self.assertEqual(anti_shuffle('123HelloWorld!!!'), '123Hello !!!Wdlor')
        self.assertEqual(anti_shuffle('123HelloWorld456'), '123Hello World456')

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including empty strings, single words, multiple words, punctuation, special characters, and numbers. It ensures that the function works correctly for various inputs and maintains the order of words and blank spaces in the sentence.