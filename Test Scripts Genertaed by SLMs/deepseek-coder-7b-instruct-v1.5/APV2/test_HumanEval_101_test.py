You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Single"), ["Single"])

    def test_comma_separated_words(self):
        self.assertEqual(words_string("Hi, my, name, is, John"), ["Hi", "my", "name", "is", "John"])

    def test_space_separated_words(self):
        self.assertEqual(words_string("Hi my name is John"), ["Hi", "my", "name", "is", "John"])

    def test_mixed_comma_and_space_separated_words(self):
        self.assertEqual(words_string("Hi, my name, is, John"), ["Hi", "my", "name", "is", "John"])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios including an empty string, a single word, words separated by commas, words separated by spaces, and a mix of both.