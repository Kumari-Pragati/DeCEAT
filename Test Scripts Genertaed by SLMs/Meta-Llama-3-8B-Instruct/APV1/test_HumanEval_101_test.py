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
        return s_list.split()assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_101_code import unknown_function

class TestWordsString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(unknown_function(""), [])

    def test_single_word(self):
        self.assertEqual(unknown_function("Hello"), ["Hello"])

    def test_multiple_words(self):
        self.assertEqual(unknown_function("Hello, World"), ["Hello", "World"])

    def test_multiple_words_with_spaces(self):
        self.assertEqual(unknown_function("Hello World"), ["Hello", "World"])

    def test_multiple_words_with_commas_and_spaces(self):
        self.assertEqual(unknown_function("Hello, World, Foo, Bar"), ["Hello", "World", "Foo", "Bar"])

    def test_multiple_words_with_punctuation(self):
        self.assertEqual(unknown_function("Hello, World! Foo, Bar?"), ["Hello", "World", "Foo", "Bar"])

    def test_multiple_words_with_punctuation_and_spaces(self):
        self.assertEqual(unknown_function("Hello, World! Foo, Bar?"), ["Hello", "World", "Foo", "Bar"])

    def test_multiple_words_with_punctuation_and_commas(self):
        self.assertEqual(unknown_function("Hello, World! Foo, Bar?"), ["Hello", "World", "Foo", "Bar"])

    def test_multiple_words_with_punctuation_and_spaces_and_commas(self):
        self.assertEqual(unknown_function("Hello, World! Foo, Bar?"), ["Hello", "World", "Foo", "Bar"])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of test cases, including:

- An empty string
- A single word
- Multiple words separated by commas
- Multiple words separated by spaces
- Multiple words separated by commas and spaces
- Multiple words with punctuation
- Multiple words with punctuation and spaces
- Multiple words with punctuation and commas
- Multiple words with punctuation, spaces, and commas