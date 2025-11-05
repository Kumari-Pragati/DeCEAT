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

 Here is a unittest test script for the `select_words` function:


import unittest
from HumanEval_117_code import select_words

class TestSelectWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(select_words("", 4), [])

    def test_one_word(self):
        self.assertEqual(select_words("word", 4), [])

    def test_one_word_with_consonants(self):
        self.assertEqual(select_words("word", 3), [])

    def test_multiple_words_with_consonants(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])

    def test_multiple_words_with_consonants_and_vowels(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test_multiple_words_with_only_vowels(self):
        self.assertEqual(select_words("aeiou", 3), [])

    def test_multiple_words_with_only_consonants(self):
        self.assertEqual(select_words("bcbdbcd", 3), ["bcb", "bcd"])

    def test_multiple_words_with_different_consonants(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test_multiple_words_with_different_consonants_and_vowels(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])

    def test_multiple_words_with_different_consonants_and_vowels_2(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to cover different scenarios, such as an empty string, one word, multiple words with consonants, multiple words with vowels, multiple words with only consonants, and multiple words with different consonants and vowels. It also includes test cases for edge cases like strings with only vowels and strings with only consonants.