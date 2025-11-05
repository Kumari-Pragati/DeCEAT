system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_101_code import unknown_function
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    if not s:
            return []

        s_list = []

        for letter in s:
            if letter == ',':
                s_list.append(' ')
            else:
                s_list.append(letter)

        s_list = "".join(s_list)
        return s_list.split()


assistant

import unittest

# Given function
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(words_string(""), [], msg="Should return empty list for empty input")

    def test_multiple_words(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"], msg="Should correctly split 'Hi, my name is John' into ['Hi', 'my', 'name', 'is', 'John']")

    def test_comma_separated(self):
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"], msg="Should correctly split 'One, two, three, four, five, six' into ['One', 'two', 'three', 'four', 'five', 'six']")

    def test_space_separated(self):
        self.assertEqual(words_string("Hello world!"), ["Hello", "world!"], msg="Should correctly split 'Hello world!' into ['Hello', 'world!']")

    def test_empty_input(self):
        self.assertEqual(words_string(), [], msg="Should return empty list for empty input")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestWordsString` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `words_string` function using assertEqual assertions. The docstring for each method describes what it tests. If any of these tests fail, the corresponding assertion will raise an error, indicating which part of the function needs further investigation.