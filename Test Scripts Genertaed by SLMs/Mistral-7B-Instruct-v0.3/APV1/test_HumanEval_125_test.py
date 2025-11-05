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

 Here is a comprehensive unittest test suite for the `split_words` function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_words_with_spaces(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello   world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello   world  !"), ["Hello", "world", "!"])

    def test_split_words_with_commas(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello, world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello, world, !"), ["Hello", "world", "!"])

    def test_split_words_without_spaces_or_commas(self):
        self.assertEqual(split_words("abcdef"), 3)
        self.assertEqual(split_words("ABCDEF"), 3)
        self.assertEqual(split_words("123456"), 0)
        self.assertEqual(split_words("ABCDEFG"), 6)
        self.assertEqual(split_words("zyxwvutsrqponmlkjihgfedcba"), 26)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_split_words_with_spaces`: Tests the function when the input string contains spaces.
2. `test_split_words_with_commas`: Tests the function when the input string contains commas.
3. `test_split_words_without_spaces_or_commas`: Tests the function when the input string does not contain spaces or commas.

Each test case includes multiple test cases to cover different scenarios. The test suite uses the `assertEqual` method to compare the expected output with the actual output produced by the `split_words` function.