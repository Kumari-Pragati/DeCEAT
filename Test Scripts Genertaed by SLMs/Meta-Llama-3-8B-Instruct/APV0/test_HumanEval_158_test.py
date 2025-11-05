user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_158_code import find_max
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    Examples:
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    """
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]assistant

Here is the unittest test script for the `find_max` function:

import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")

    def test_example2(self):
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")

    def test_example3(self):
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_empty_list(self):
        self.assertRaises(IndexError, find_max, [])

    def test_single_element_list(self):
        self.assertEqual(find_max(["hello"]), "hello")

    def test_multiple_max(self):
        self.assertEqual(find_max(["abc", "def", "ghi"]), "abc")

    def test_tie_breaker(self):
        self.assertEqual(find_max(["abc", "def", "abcde"]), "abcde")

if __name__ == '__main__':
    unittest.main()

This test script covers the following scenarios:

1. The three examples provided in the problem statement.
2. An empty list, which should raise an IndexError.
3. A list with a single element, which should return that element.
4. A list with multiple elements that have the maximum number of unique characters, where the function should return the one that comes first in lexicographical order.
5. A list with multiple elements that have the maximum number of unique characters, where the function should return the one that comes first in lexicographical order, and there is a tie (i.e., two or more elements have the same maximum number of unique characters).

You can run this script directly to execute the tests.