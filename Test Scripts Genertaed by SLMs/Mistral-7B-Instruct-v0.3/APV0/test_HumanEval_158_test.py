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
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]

 Here is a unittest test script for the `find_max` function:


import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")
        self.assertEqual(find_max(["aa", "ab", "ac", "ba", "bb", "bc"]), "ba")
        self.assertEqual(find_max(["aa", "ab", "ac", "ba", "bb", "bc", "aaa"]), "aaa")
        self.assertEqual(find_max(["", "a"]), "a")
        self.assertEqual(find_max(["aa", ""]), "aa")
        self.assertEqual(find_max(["", ""]), "")

if __name__ == '__main__':
    unittest.main()


This test script includes multiple test cases to ensure the function works correctly for various inputs. It tests the edge cases, such as empty strings, single characters, and multiple words with the same number of unique characters.