You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max_lexicographical(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")

    def test_find_max_lexicographical_ties(self):
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")

    def test_find_max_longest_unique_chars(self):
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_find_max_empty_list(self):
        self.assertEqual(find_max([]), "")

    def test_find_max_single_element(self):
        self.assertEqual(find_max(["a"]), "a")

    def test_find_max_single_word(self):
        self.assertEqual(find_max(["string"]), "string")

    def test_find_max_same_length_unique_chars(self):
        self.assertEqual(find_max(["abc", "abd", "abce"]), "abce")

    def test_find_max_same_length_unique_chars_ties(self):
        self.assertEqual(find_max(["abc", "abd", "acb"]), "abc")

    def test_find_max_same_length_unique_chars_ties_lexicographical(self):
        self.assertEqual(find_max(["abc", "acb", "bac"]), "abc")

    def test_find_max_mixed_case(self):
        self.assertEqual(find_max(["Name", "of", "String"]), "String")

    def test_find_max_mixed_case_ties(self):
        self.assertEqual(find_max(["Name", "enam", "Game"]), "enam")

if __name__ == '__main__':
    unittest.main()