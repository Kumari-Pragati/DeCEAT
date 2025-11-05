user

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
    return resultassistant

Here is the unittest test script for the `all_prefixes` function:

import unittest
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_single_char_string(self):
        self.assertEqual(all_prefixes("a"), ["a"])

    def test_short_string(self):
        self.assertEqual(all_prefixes("abc"), ["a", "ab", "abc"])

    def test_medium_string(self):
        self.assertEqual(all_prefixes("abcdef"), ["a", "ab", "abc", "abcd", "abcde", "abcdef"])

    def test_long_string(self):
        self.assertEqual(all_prefixes("abcdefghijklmnopqrstuvwxyz"), 
                         ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi", 
                          "abcdefghj", "abcdefghk", "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn", 
                          "abcdefghijklmno", "abcdefghijklmnop", "abcdefghijklmnopq", "abcdefghijklmnopqr", 
                          "abcdefghijklmnopqrs", "abcdefghijklmnopqrst", "abcdefghijklmnopqrstu", 
                          "abcdefghijklmnopqrtuv", "abcdefghijklmnopqrstuv", "abcdefghijklmnopqrstuvw", 
                          "abcdefghijklmnopqrstuvwx", "abcdefghijklmnopqrstuvwxy", "abcdefghijklmnopqrstxyz", 
                          "abcdefghijklmnopqrstxyzab", "abcdefghijklmnopqrstxyzabc", "abcdefghijklmnopqrstxyzabcd", 
                          "abcdefghijklmnopqrstxyzabcde", "abcdefghijklmnopqrstxyzabcdef", "abcdefghijklmnopqrstxyzabcdefg", 
                          "abcdefghijklmnopqrstxyzabcdefgh", "abcdefghijklmnopqrstxyzabcdefghi", "abcdefghijklmnopqrstxyzabcdefghj", 
                          "abcdefghijklmnopqrstxyzabcdefghk", "abcdefghijklmnopqrstxyzabcdefghijkl", "abcdefghijklmnopqrstxyzabcdefghijklm", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmn", "abcdefghijklmnopqrstxyzabcdefghijklmno", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnop", "abcdefghijklmnopqrstxyzabcdefghijklmnopq", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqr", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrs", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrst", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstu", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrtuv", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstuv", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstuvw", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstuvwx", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstuvwxy", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyz", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzab", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabc", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcd", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcde", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdef", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefg", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefgh", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghi", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghj", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghk", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijkl", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklm", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmn", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmno", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnop", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopq", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqr", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqrs", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqrst", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqrstu", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqrtuv", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqrstuv", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqrstuvw", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqrstuvwx", 
                          "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqrstuvwxy", "abcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyzabcdefghijklmnopqrstxyz"])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            all_prefixes(123)

if __name__ == '__main__':
    unittest.main()

This test script covers the following cases:

1. An empty string
2. A single-character string
3. A short string (e.g., "abc")
4. A medium-length string (e.g., "abcdef")
5. A long string (e.g., "abcdefghijklmnopqrstuvwxyz")
6. An invalid input (e.g., an integer instead of a string)

Each test case uses the `assertEqual` method to verify that the output of the `all_prefixes` function matches the expected result. The `assertRaises` method is used to test that the function raises a `TypeError` when given an invalid input (in this case, an integer).