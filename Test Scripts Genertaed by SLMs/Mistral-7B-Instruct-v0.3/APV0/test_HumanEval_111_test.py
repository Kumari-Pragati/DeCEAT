Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_111_code import histogram
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """

    dict1 = {}
    list1 = test.split(" ")
    t = 0

    for i in list1:
        if (list1.count(i) > t) and i != '':
            t = list1.count(i)
    if t > 0:
        for i in list1:
            if list1.count(i) == t:
                dict1[i] = t
    return dict1

 Here is a unittest test script for the provided function `histogram`. The test cases cover various scenarios, including an empty string, single-letter words, multiple occurrences of the same letter, and multiple letters with the same maximum occurrence.


import unittest
from HumanEval_111_code import histogram

class TestHistogram(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(histogram(''), {})

    def test_single_letter_words(self):
        self.assertEqual(histogram('a'), {'a': 1})
        self.assertEqual(histogram('b'), {'b': 1})
        self.assertEqual(histogram('c'), {'c': 1})

    def test_multiple_occurrences(self):
        self.assertEqual(histogram('a a'), {'a': 2})
        self.assertEqual(histogram('b b'), {'b': 2})
        self.assertEqual(histogram('c c'), {'c': 2})

    def test_multiple_letters_same_max_occurrence(self):
        self.assertEqual(histogram('a b a'), {'a': 2, 'b': 1})
        self.assertEqual(histogram('b a b'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('c a b'), {'a': 2, 'b': 1, 'c': 1})

    def test_multiple_letters_same_max_occurrence_multiple_max(self):
        self.assertEqual(histogram('a b a b'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('b a b a'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('c a b a'), {'a': 2, 'b': 1, 'c': 1})

if __name__ == '__main__':
    unittest.main()


This script includes a `TestHistogram` class that contains several test methods. Each test method tests a specific scenario, and the `assertEqual` method is used to check if the function's output matches the expected output. The script ends with the standard boilerplate for running the tests.