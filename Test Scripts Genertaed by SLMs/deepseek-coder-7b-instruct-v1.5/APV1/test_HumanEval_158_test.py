You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")
        self.assertEqual(find_max(["abc", "def", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "abcd", "abcde"]), "abcd")
        self.assertEqual(find_max(["abc", "def", "ghijklmn"]), "ghijklmn")
        self.assertEqual(find_max(["123456", "789", "0"]), "123456")
        self.assertEqual(find_max(["123", "1234", "12345"]), "1234")
        self.assertEqual(find_max(["abc", "def", "ghi", "jkl"]), "abc")
        self.assertEqual(find_max(["abc", "def", "ghi", "jkl", "mno"]), "mno")

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the `find_max` function is working correctly. It tests with words of different lengths, including words with unique characters, words with duplicate characters, and words in lexicographical order.