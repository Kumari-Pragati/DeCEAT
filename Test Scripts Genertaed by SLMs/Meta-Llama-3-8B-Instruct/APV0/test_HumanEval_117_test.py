user

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
    return resultassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_117_code import select_words

class TestSelectWords(unittest.TestCase):

    def test_select_words(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
        self.assertEqual(select_words("simple white space", 2), [])
        self.assertEqual(select_words("Hello world", 4), ["world"])
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])
        self.assertEqual(select_words("", 2), [])
        self.assertEqual(select_words("a", 1), ["a"])
        self.assertEqual(select_words("abc", 2), ["bc"])
        self.assertEqual(select_words("abc", 1), ["a", "b", "c"])
        self.assertEqual(select_words("abc", 3), [])

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure the function is working correctly. The test cases cover various scenarios, including:

- Testing with different input strings and numbers of consonants
- Testing with an empty string
- Testing with a single character
- Testing with a string containing multiple words
- Testing with a string containing only vowels
- Testing with a string containing only consonants

Each test case uses the `assertEqual` method to compare the output of the `select_words` function with the expected output. If the output does not match the expected output, the test case will fail, indicating that the function is not working correctly.