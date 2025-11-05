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

 import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_on_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_on_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_count_lowercase_odd_order_letters(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_empty_string(self):
        self.assertEqual(split_words(""), [])

    def test_no_whitespace_or_comma(self):
        self.assertEqual(split_words("abc123"), 0)

    def test_all_whitespace(self):
        self.assertEqual(split_words("   "), [])

    def test_all_commas(self):
        self.assertEqual(split_words(",,,,"), [])

    def test_mixed_whitespace_and_commas(self):
        self.assertEqual(split_words("Hello,,world!"), ["Hello", "world!"])

    def test_mixed_whitespace_and_letters(self):
        self.assertEqual(split_words("Hello 123 world!"), ["Hello", "123", "world!"])

if __name__ == '__main__':
    unittest.main()