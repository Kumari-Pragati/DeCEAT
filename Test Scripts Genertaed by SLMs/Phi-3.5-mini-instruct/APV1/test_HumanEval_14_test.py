You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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
        self.assertEqual(all_prefixes(''), [])

    def test_single_character(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_characters(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_alphabetical_string(self):
        self.assertEqual(all_prefixes('xyz'), ['x', 'xy', 'xyz'])

    def test_repeated_characters(self):
        self.assertEqual(all_prefixes('aaa'), ['a', 'aa', 'aaa'])

    def test_special_characters(self):
        self.assertEqual(all_prefixes('!@#'), ['!', '!@', '!@#'])

    def test_whitespace(self):
        self.assertEqual(all_prefixes(' '), [' ', ' '])

    def test_empty_list(self):
        self.assertEqual(all_prefixes(''), [])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            all_prefixes(123)

if __name__ == '__main__':
    unittest.main()