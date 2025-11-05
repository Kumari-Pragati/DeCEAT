You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):
    def test_with_whitespaces(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_with_commas(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_with_no_whitespaces_or_commas(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_with_mixed_case(self):
        self.assertEqual(split_words("abcDeF"), 3)

    def test_with_special_characters(self):
        self.assertEqual(split_words("abc!def"), 3)

    def test_with_numbers(self):
        self.assertEqual(split_words("abc123def"), 3)

    def test_with_empty_string(self):
        self.assertEqual(split_words(""), [])

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios:

1. When the input string contains whitespaces.
2. When the input string contains commas.
3. When the input string contains neither whitespaces nor commas.
4. When the input string contains mixed case letters.
5. When the input string contains special characters.
6. When the input string contains numbers.
7. When the input string is an empty string.

Each test checks that the output of the `split_words` function matches the expected output.