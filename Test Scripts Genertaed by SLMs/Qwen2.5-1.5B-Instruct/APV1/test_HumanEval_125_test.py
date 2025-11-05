system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
    
    def test_split_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_no_whitespace_or_comma(self):
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestSplitWords` class that inherits from `unittest.TestCase`. It contains three methods to test different cases of the `split_words` function:

- `test_split_whitespace`: Tests the case where there are spaces in the input string.
- `test_split_comma`: Tests the case where there are commas in the input string.
- `test_no_whitespace_or_comma`: Tests the case where neither spaces nor commas exist in the input string.

The `assertEqual` method checks if the output of the `split_words` function matches the expected result. If any of these tests fail, an assertion error will be raised.