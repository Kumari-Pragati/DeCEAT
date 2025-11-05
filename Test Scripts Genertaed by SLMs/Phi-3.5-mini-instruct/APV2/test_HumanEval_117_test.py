You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 import unittest
from HumanEval_117_code import select_words

class TestSelectWords(unittest.TestCase):

    def test_select_words_with_four_consonants(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])

    def test_select_words_with_three_consonants(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test_select_words_with_no_matching_words(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test_select_words_with_four_consonants_in_single_word(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])

    def test_select_words_with_three_consonants_in_single_word(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

    def test_select_words_with_empty_string(self):
        self.assertEqual(select_words("", 0), [])

    def test_select_words_with_non_letter_characters(self):
        self.assertEqual(select_words("123 abc", 2), [])

    def test_select_words_with_mixed_case_letters(self):
        self.assertEqual(select_words("Mary Had A Little Lamb", 4), ["little"])

if __name__ == '__main__':
    unittest.main()