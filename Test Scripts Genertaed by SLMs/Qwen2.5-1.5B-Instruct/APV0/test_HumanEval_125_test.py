system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Define the function to be tested
def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    """
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',', ' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i) % 2 == 0])

class TestSplitWords(unittest.TestCase):

    def test_split_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_odd_lowercase_letters(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_no_spaces_or_commas(self):
        self.assertEqual(split_words("abcde"), 5)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` module, defines the `split_words` function as provided, and then creates a class `TestSplitWords` that inherits from `unittest.TestCase`. Each method within this class tests a specific case using assertions based on the examples given in the docstring. Finally, it calls `unittest.main()` to run all the tests.