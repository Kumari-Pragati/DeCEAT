You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_74_code import total_match
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    If the two lists have the same number of chars, return the first list.

    Examples:
        total_match([], []) ➞ []
        total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
        total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
        total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
        total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    l1 = 0
    for st in lst1:
        l1 += len(st)

    l2 = 0
    for st in lst2:
        l2 += len(st)

    if l1 <= l2:
        return lst1
    else:
        return lst2

 Here is the complete unittest test suite for the `total_match` function:


import unittest
from HumanEval_74_code import total_match

class TestTotalMatch(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])

    def test_one_string_each(self):
        self.assertEqual(total_match(['hi'], ['hI']), ['hI'])
        self.assertEqual(total_match(['hI'], ['hi']), ['hI'])

    def test_different_lengths(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

    def test_same_lengths(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])
        self.assertEqual(total_match(['hI', 'hi', 'hi'], ['hi', 'hI', 'hI']), ['hI', 'hi', 'hi'])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as empty lists, one string each, different lengths, and same lengths. The test suite uses the `unittest.TestCase` class to define test methods with the `self.assertEqual()` method to verify the expected and actual results.