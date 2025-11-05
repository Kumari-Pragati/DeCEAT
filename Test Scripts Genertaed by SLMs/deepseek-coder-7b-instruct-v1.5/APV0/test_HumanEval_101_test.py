You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given Python function:


import unittest
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_multiple_words(self):
        self.assertEqual(words_string("Hello, world"), ["Hello", "world"])

    def test_multiple_words_with_comma(self):
        self.assertEqual(words_string("Hello, world, how, are, you"), ["Hello", "world", "how", "are", "you"])

    def test_multiple_words_with_space(self):
        self.assertEqual(words_string("Hello world how are you"), ["Hello", "world", "how", "are", "you"])

    def test_multiple_words_with_comma_and_space(self):
        self.assertEqual(words_string("Hello, world, how, are, you"), ["Hello", "world", "how", "are", "you"])

if __name__ == '__main__':
    unittest.main()


This script tests the `words_string` function with various inputs, including empty strings, strings with a single word, strings with multiple words separated by commas or spaces, and strings with both commas and spaces.

Please note that the `HumanEval_101_code` module and the `words_string` function should be defined elsewhere in your code.