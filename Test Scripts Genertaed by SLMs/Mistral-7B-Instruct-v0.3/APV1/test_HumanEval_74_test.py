You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `total_match` function:


import unittest
from HumanEval_74_code import total_match

class TestTotalMatch(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])

    def test_one_string_in_each_list(self):
        self.assertEqual(total_match(['hi'], ['hI']), ['hI'])
        self.assertEqual(total_match(['hI'], ['hi']), ['hI'])

    def test_different_lengths(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])
        self.assertEqual(total_match(['hI', 'Hi'], ['hi', 'admin']), ['hI', 'Hi'])

    def test_same_lengths_different_strings(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi']), ['hi', 'hi'])
        self.assertEqual(total_match(['hI', 'Hi'], ['hi', 'hi']), ['hI', 'Hi'])

    def test_same_lengths_different_cases(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'ADMIN']), ['hI', 'ADMIN'])
        self.assertEqual(total_match(['hI', 'ADMIN'], ['hi', 'admin']), ['hI', 'ADMIN'])

    def test_one_string_longer(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin']), ['hi', 'admin'])
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_one_string_shorter(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as empty lists, one string in each list, different lengths, same lengths with different strings, same lengths with different cases, one list having one string and the other having multiple strings, and one list having a shorter string than the other.