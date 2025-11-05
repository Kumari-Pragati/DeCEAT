You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the provided `histogram` function:


import unittest
from HumanEval_111_code import histogram

class TestHistogram(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(histogram(''), {})

    def test_single_letter(self):
        self.assertEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})

    def test_repeated_letters(self):
        self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})

    def test_multiple_max_occurrences(self):
        self.assertEqual(histogram('b b b b a'), {'b': 4})

    def test_multiple_max_occurrences_different_letters(self):
        self.assertEqual(histogram('a b c d a b'), {'a': 2, 'b': 2})

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios, such as an empty string, single letters, repeated letters, multiple letters with the same maximum occurrence, and multiple letters with different maximum occurrences. The test suite uses the `unittest.TestCase` class to define test methods and the `assertEqual` method to compare the expected and actual results.