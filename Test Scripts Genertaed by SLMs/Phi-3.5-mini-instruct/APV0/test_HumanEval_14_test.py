Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

    def test_full_string(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_string_with_spaces(self):
        self.assertEqual(all_prefixes('abc def'), ['a', 'ab', 'abc', 'a', 'ab', 'abc', 'a', 'ab', 'abc def'])

    def test_string_with_special_characters(self):
        self.assertEqual(all_prefixes('abc!'), ['a', 'ab', 'abc', 'a!'])

    def test_repeated_characters(self):
        self.assertEqual(all_prefixes('aaa'), ['a', 'aa', 'aaa'])

    def test_reversed_string(self):
        self.assertEqual(all_prefixes('cba'), ['c', 'cb', 'cba'])

    def test_case_sensitivity(self):
        self.assertEqual(all_prefixes('ABC'), ['A', 'AB', 'ABC'])

if __name__ == '__main__':
    unittest.main()