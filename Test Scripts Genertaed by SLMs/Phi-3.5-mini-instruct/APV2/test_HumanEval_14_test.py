You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_14_code import all_prefixes
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result: List[str] = []
    for i in range(len(string)):
        result.append(string[: i + 1])
    return result

 
import unittest
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [''])

    def test_single_character(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_characters(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_long_string(self):
        self.assertEqual(all_prefixes('abcdefghijklmnopqrstuvwxyz'), ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 'abcdefghijklmnopqrstuvwxyz'])

    def test_special_characters(self):
        self.assertEqual(all_prefixes('!@#$%^&*()'), ['!', '!@', '!@#', '!@#$', '!@#$%', '!@#$%^', '!@#$%^&', '!@#$%^&*', '!@#$%^&*()'])

    def test_whitespace(self):
        self.assertEqual(all_prefixes(' '), [' ', ' ', '  '])

    def test_repeated_characters(self):
        self.assertEqual(all_prefixes('aaa'), ['a', 'aa', 'aaa'])

    def test_non_alphanumeric(self):
        self.assertEqual(all_prefixes('123!'), ['1', '12', '123', '123!'])

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `all_prefixes` function, including empty strings, single characters, multiple characters, long strings, special characters, whitespace, repeated characters, and non-alphanumeric characters. Each test case checks if the function returns the expected list of prefixes. Running this test suite will validate the correctness of the `all_prefixes` function.