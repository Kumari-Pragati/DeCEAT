You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 import unittest
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_words_string_with_commas(self):
        input_str = "Hi, my name is John"
        expected_output = ["Hi", "my", "name", "is", "John"]
        self.assertEqual(words_string(input_str), expected_output)

    def test_words_string_with_spaces(self):
        input_str = "One two three four five six"
        expected_output = ["One", "two", "three", "four", "five", "six"]
        self.assertEqual(words_string(input_str), expected_output)

    def test_words_string_empty_string(self):
        input_str = ""
        expected_output = []
        self.assertEqual(words_string(input_str), expected_output)

    def test_words_string_with_no_separators(self):
        input_str = "HelloWorld"
        expected_output = ["HelloWorld"]
        self.assertEqual(words_string(input_str), expected_output)

    def test_words_string_with_multiple_spaces(self):
        input_str = "  Hello   World  "
        expected_output = ["Hello", "World"]
        self.assertEqual(words_string(input_str), expected_output)

    def test_words_string_with_special_characters(self):
        input_str = "Hello! World?"
        expected_output = ["Hello", "World"]
        self.assertEqual(words_string(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()