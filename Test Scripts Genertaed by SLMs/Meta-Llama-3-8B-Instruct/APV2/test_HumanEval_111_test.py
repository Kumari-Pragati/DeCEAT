system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
        if (list1.count(i) > t) and i!= '':
            t = list1.count(i)
    if t > 0:
        for i in list1:
            if list1.count(i) == t:
                dict1[i] = t
    return dict1assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_111_code import histogram

class TestHistogram(unittest.TestCase):

    def test_histogram(self):
        self.assertEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('b b b b a'), {'b': 4})
        self.assertEqual(histogram(''), {})

    def test_histogram_empty_string(self):
        self.assertEqual(histogram(''), {})

    def test_histogram_single_letter(self):
        self.assertEqual(histogram('a'), {'a': 1})

    def test_histogram_multiple_letters(self):
        self.assertEqual(histogram('a b c d'), {'a': 1, 'b': 1, 'c': 1, 'd': 1})

    def test_histogram_repeated_letters(self):
        self.assertEqual(histogram('a a a'), {'a': 3})
        self.assertEqual(histogram('b b b b b'), {'b': 5})

    def test_histogram_multiple_repeated_letters(self):
        self.assertEqual(histogram('a a a b b b'), {'a': 3, 'b': 3})

if __name__ == '__main__':
    unittest.main()