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

 import unittest
from HumanEval_111_code import histogram

class TestHistogramFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(histogram(''), {})

    def test_single_letter(self):
        self.assertEqual(histogram('a'), {'a': 1})

    def test_multiple_letters_unique(self):
        self.assertEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})

    def test_multiple_letters_same_count(self):
        self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})

    def test_multiple_letters_different_counts(self):
        self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2, 'c': 1})

    def test_multiple_letters_single_max_count(self):
        self.assertEqual(histogram('b b b b a'), {'b': 4})

    def test_multiple_letters_multiple_max_counts(self):
        self.assertEqual(histogram('a b b a b b'), {'a': 2, 'b': 3})

if __name__ == '__main__':
    unittest.main()