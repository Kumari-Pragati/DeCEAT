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

 Here is a unittest test script for the `all_prefixes` function:


import unittest
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [''])

    def test_single_character_string(self):
        self.assertListEqual(all_prefixes('a'), ['a'])
        self.assertListEqual(all_prefixes('b'), ['b'])
        self.assertListEqual(all_prefixes('c'), ['c'])

    def test_multi_character_string(self):
        self.assertListEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertListEqual(all_prefixes('abcd'), ['a', 'ab', 'abc', 'abcd'])
        self.assertListEqual(all_prefixes('xyz'), ['x', 'xy', 'xyz'])

if __name__ == '__main__':
    unittest.main()


This test script includes three test cases:

1. An empty string: `all_prefixes('')` should return a list containing an empty string `[]`.
2. Single character strings: `all_prefixes('a')`, `all_prefixes('b')`, and `all_prefixes('c')` should return lists containing the respective single character string.
3. Multi-character strings: `all_prefixes('abc')`, `all_prefixes('abcd')`, and `all_prefixes('xyz')` should return lists containing all possible prefixes of the given strings.

You can run this test script directly by saving it as a .py file and running it using the command `python filename.py`.