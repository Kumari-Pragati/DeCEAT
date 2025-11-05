You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_words_with_space(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_words_with_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_with_lowercase_letters(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_split_words_with_no_whitespace_or_comma(self):
        self.assertEqual(split_words("HelloWorld!"), ["HelloWorld!"])

    def test_split_words_with_uppercase_letters(self):
        self.assertEqual(split_words("HELLO WORLD!"), ["HELLO", "WORLD!"])

    def test_split_words_with_mixed_case_letters(self):
        self.assertEqual(split_words("HeLlO WoRlD!"), ["HeLlO", "WoRlD!"])

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure that the `split_words` function behaves as expected in various scenarios.

Please note that the `split_words` function is not designed to handle mixed case letters in the same way as it handles lowercase letters. The function only counts lowercase letters with odd order in the alphabet, so "HeLlO WoRlD!" would return 2, not 5. If you want to count uppercase letters as well, you would need to modify the function to handle this.

Also, the `split_words` function does not handle punctuation marks. If you want to test this, you would need to add additional test cases.