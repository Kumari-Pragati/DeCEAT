You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_117_code import select_words
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a", "e", "i", "o", "u"]:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_117_code import select_words

class TestSelectWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(select_words("", 4), [])

    def test_no_matching_words(self):
        self.assertEqual(select_words("Mary had a little lamb", 2), [])

    def test_single_matching_word(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])

    def test_multiple_matching_words(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test_case_insensitive(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

    def test_spaces_in_string(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test_consonants_in_word(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestSelectWords` that contains several test methods. Each method tests a specific scenario. The `unittest.main()` function is called at the end, which runs all the test methods when the script is run directly.

Please note that you need to have the function `select_words` implemented in the file `HumanEval_117_code.py` for these tests to work.