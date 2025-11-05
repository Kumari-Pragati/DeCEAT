You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_51_code import remove_vowels

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])

 Here is a comprehensive unittest test suite for the `remove_vowels` function:


import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_single_letter(self):
        for char in ['b', 'c', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
            self.assertEqual(remove_vowels(char), char)

    def test_multiple_letters(self):
        test_cases = [
            ("abcdef\nghijklm", "bcdf\nghjklm"),
            ("abcdef", "bcdf"),
            ("aaaaa", ''),
            ("aaBAA", 'B'),
            ("zbcd", "zbcd")
        ]
        for test_case in test_cases:
            self.assertEqual(remove_vowels(test_case[0]), test_case[1])

    def test_mixed_case(self):
        test_cases = [
            ("ABCDEF", "BCDF"),
            ("aBcDeF", "BcDf"),
            ("AaBbCcDdEe", "BbCcDd"),
            ("123abc456def789", "123bcd789")
        ]
        for test_case in test_cases:
            self.assertEqual(remove_vowels(test_case[0]), test_case[1])

    def test_special_characters(self):
        test_cases = [
            ("!@#$%^&*()_+-=[]{}|;:'\",.<>?/", "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"),
            ("abc!def", "bcd!f"),
            ("abc@def", "bcd@f"),
            ("abc#def", "bcd#f"),
            ("abc$def", "bcd$f")
        ]
        for test_case in test_cases:
            self.assertEqual(remove_vowels(test_case[0]), test_case[1])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty string, single letters, multiple letters, mixed case, and special characters. It covers various edge cases and ensures that the function behaves as expected.