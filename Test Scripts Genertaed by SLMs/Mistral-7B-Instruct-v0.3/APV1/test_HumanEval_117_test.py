You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `select_words`.


import unittest
from HumanEval_117_code import select_words

class TestSelectWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(select_words("", 4), [])

    def test_no_matching_words(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test_one_matching_word(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

    def test_multiple_matching_words(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
        self.assertEqual(select_words("Hello world", 4), ["world"])

    def test_exact_match(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty string, no matching words, one matching word, multiple matching words, and exact matching words. The test cases cover various scenarios to ensure the function behaves as expected.