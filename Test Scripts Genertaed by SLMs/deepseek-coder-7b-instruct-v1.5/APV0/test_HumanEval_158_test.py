You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")
        self.assertEqual(find_max(["apple", "banana", "cherry"]), "banana")
        self.assertEqual(find_max(["abc", "def", "ghi"]), "abc")
        self.assertEqual(find_max(["123", "456", "789"]), "123")
        self.assertEqual(find_max(["aaa", "bbb", "ccc"]), "aaa")
        self.assertEqual(find_max(["zyx", "wvu", "tsr"]), "zyx")
        self.assertEqual(find_max(["dog", "cat", "mouse"]), "dog")
        self.assertEqual(find_max(["elephant", "bear", "lion"]), "elephant")

if __name__ == '__main__':
    unittest.main()


This script tests the `find_max` function with a variety of inputs to ensure that it is working as expected. It checks that the function returns the correct word for each input.

Please note that the `HumanEval_158_code` module should contain the `find_max` function for this script to work.