You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_125_code import split_words
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',', ' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i) % 2 == 0])

 
import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_words_with_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_words_with_commas(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_with_no_whitespace_or_commas(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_split_words_empty_string(self):
        self.assertEqual(split_words(""), [])

    def test_split_words_single_word(self):
        self.assertEqual(split_words("Hello"), ["Hello"])

    def test_split_words_multiple_words_with_spaces(self):
        self.assertEqual(split_words("Hello   world!"), ["Hello", "world!"])

    def test_split_words_multiple_words_with_commas(self):
        self.assertEqual(split_words("Hello,   world!"), ["Hello", "world!"])

    def test_split_words_lowercase_letters_with_odd_order(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_split_words_special_characters(self):
        self.assertEqual(split_words("Hello! world"), ["Hello!", "world"])

    def test_split_words_uppercase_letters(self):
        self.assertEqual(split_words("Hello World"), 0)

    def test_split_words_numbers(self):
        self.assertEqual(split_words("12345"), 0)

    def test_split_words_mixed_case_letters(self):
        self.assertEqual(split_words("HelloWorld"), 0)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `split_words` function, including strings with whitespace, commas, no whitespace or commas, empty strings, single words, multiple words with spaces, multiple words with commas, lowercase letters with odd order, special characters, uppercase letters, numbers, and mixed case letters. Each test case ensures that the function behaves as expected for different types of input.