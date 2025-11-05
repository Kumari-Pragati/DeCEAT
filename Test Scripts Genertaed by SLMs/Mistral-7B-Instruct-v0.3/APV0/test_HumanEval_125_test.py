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

 Here is a unittest test script for the `split_words` function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):
    def test_split_words_with_spaces(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("  Hello world!  "), ["Hello", "world!"])
        self.assertEqual(split_words("   Hello   world   !   "), ["Hello", "world"])

    def test_split_words_with_commas(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello, world,!"), ["Hello", "world"])
        self.assertEqual(split_words("Hello,,world,,!"), ["Hello", "world"])

    def test_split_words_no_spaces_or_commas(self):
        self.assertEqual(split_words("abcdef"), 3)
        self.assertEqual(split_words("ABCDEF"), 3)
        self.assertEqual(split_words("123456"), 0)
        self.assertEqual(split_words("ZYXWVUT"), 0)

    def test_split_words_empty_string(self):
        self.assertEqual(split_words(""), 0)

    def test_split_words_special_characters(self):
        self.assertEqual(split_words("Hello,123world!"), ["Hello", "123", "world"])
        self.assertEqual(split_words("Hello_123world!"), ["Hello", "123", "world"])
        self.assertEqual(split_words("Hello$123world!"), ["Hello", "123", "world"])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases for different scenarios, such as strings with spaces, strings with commas, strings without any whitespace or commas, an empty string, and strings with special characters. It also tests the edge case where the input string consists only of uppercase letters.