You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):

    def test_single_char(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_chars(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [])

    def test_long_string(self):
        self.assertEqual(all_prefixes('abcdefghijklmnopqrstuvwxyz'), 
                         ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 
                          'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 
                          'abcdefghijkl', 'abcdefghijklm', 'abcdefghijklmn', 
                          'abcdefghijklmno', 'abcdefghijklmnop', 'abcdefghijklmnopq', 
                          'abcdefghijklmnopqr', 'abcdefghijklmnopqrs', 
                          'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu', 
                          'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw', 
                          'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy', 
                          'abcdefghijklmnopqrstuvwxyz'])

if __name__ == '__main__':
    unittest.main()


This suite includes tests for single character strings, multiple character strings, empty strings, and long strings. It checks that the function returns the correct list of prefixes for each of these cases.