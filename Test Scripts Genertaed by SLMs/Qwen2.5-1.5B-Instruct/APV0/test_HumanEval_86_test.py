system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Function to be tested
from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(anti_shuffle(""), "")

    def test_single_word(self):
        self.assertEqual(anti_shuffle("Hi"), "Hi")

    def test_multiple_words(self):
        self.assertEqual(anti_shuffle("hello world!"), "ehllo !worl dl!")

    def test_special_characters(self):
        self.assertEqual(anti_shuffle("Hello World!!!"), "Hello !!!Wdlor")

    def test_spaces_between_words(self):
        self.assertEqual(anti_shuffle("This  is   a test"), "Thi si  ai tset")

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestAntiShuffle` that inherits from `unittest.TestCase`. It contains several test methods to ensure the `anti_shuffle` function works as expected across different scenarios, including empty strings, single-word strings, multiple-word strings, special characters, and spaces between words. The `assertEqual` method checks if the output matches the expected result. Finally, the `unittest.main()` call runs all the tests when the script is executed directly.