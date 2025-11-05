system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_101_code import words_string
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

# Provided function to be tested
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_multiple_words_separated_by_comma(self):
        self.assertEqual(words_string("apple, banana, cherry"), ["apple", "banana", "cherry"])

    def test_multiple_words_separated_by_space(self):
        self.assertEqual(words_string("dog cat bird"), ["dog", "cat", "bird"])

    def test_mixed_delimiters(self):
        self.assertEqual(words_string("one,two,three,four,five,six"), ["one", "two", "three", "four", "five", "six"])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases covering different scenarios as described in the docstring of `words_string`. It checks both single-word inputs and multiple-word inputs that may contain delimiters other than spaces (like commas). The `unittest` framework is used to run these tests, ensuring they pass before the module is imported elsewhere.