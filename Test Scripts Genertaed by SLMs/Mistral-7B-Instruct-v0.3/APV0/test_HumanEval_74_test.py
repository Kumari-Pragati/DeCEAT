Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `total_match` function:


import unittest
from HumanEval_74_code import total_match

class TestTotalMatch(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])

    def test_one_string_in_each_list(self):
        self.assertEqual(total_match(['hi'], ['hI']), ['hI'])
        self.assertEqual(total_match(['hI'], ['hi']), ['hi'])

    def test_multiple_strings_in_each_list(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_list_with_single_string_vs_list_with_multiple_strings(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])
        self.assertEqual(total_match(['1'], ['1', '2', '3', '4', '5']), ['1'])
        self.assertEqual(total_match(['1', '2'], ['1']), ['1', '2'])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as empty lists, one string in each list, multiple strings in each list, and a list with a single string vs a list with multiple strings. The test cases use the `assertEqual` method to check if the expected output matches the actual output of the `total_match` function.