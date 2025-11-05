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
    alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',','').split()
    else:
        return len([i for i in txt if i.islower() and ord(i) % 2 == 0])assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_words_with_spaces(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_words_with_commas(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_with_no_spaces_or_commas(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_split_words_with_mixed_spaces_and_commas(self):
        self.assertEqual(split_words("Hello, world!"), ["Hello", "world!"])

    def test_split_words_with_no_spaces_or_commas_and_no_lowercase_letters(self):
        self.assertEqual(split_words("ABCDEF"), 0)

    def test_split_words_with_no_spaces_or_commas_and_lowercase_letters(self):
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()


This script includes six test cases to cover different scenarios:

- Test cases for splitting words with spaces and commas
- Test case for splitting words with no spaces or commas
- Test case for mixed spaces and commas
- Test case for no spaces or commas and no lowercase letters
- Test case for no spaces or commas and lowercase letters

Each test case checks if the output of the `split_words` function is as expected.