You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):
    def test_with_spaces(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_with_commas(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_with_no_whitespace_or_comma(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_with_mixed_case(self):
        self.assertEqual(split_words("AbCdEf"), 3)

    def test_with_special_characters(self):
        self.assertEqual(split_words("Hello, world!"), ["Hello", "world!"])

    def test_with_numbers(self):
        self.assertEqual(split_words("123456"), 3)

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios:

1. When the input string contains spaces.
2. When the input string contains commas.
3. When the input string contains neither spaces nor commas.
4. When the input string contains mixed case letters.
5. When the input string contains special characters.
6. When the input string contains only numbers.

Please note that the function `split_words` is expected to return a list of words when the input string contains spaces or commas, and a number when the input string contains neither spaces nor commas. The tests are written based on this expected behavior.

Also, the test `test_with_mixed_case` is checking that the function correctly counts lower-case letters with odd order in the alphabet, which is the case when the input string contains only lower-case letters.

The test `test_with_numbers` is checking that the function correctly counts lower-case letters with odd order in the alphabet, which is the case when the input string contains only numbers.

Please replace `HumanEval_125_code` with the actual module name where the `split_words` function is defined.