user

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
        return lst2assistant

Here is the unittest test script for the `total_match` function:

import unittest
from HumanEval_74_code import total_match

class TestTotalMatch(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])

    def test_same_length(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_first_list_shorter(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_second_list_shorter(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_first_list_longer(self):
        self.assertEqual(total_match(['hi', 'admin'], ['1', '2', '3', '4', '5']), ['4'])

    def test_second_list_longer(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

    def test_single_element_lists(self):
        self.assertEqual(total_match(['hi'], ['hI']), ['hi'])
        self.assertEqual(total_match(['hi'], ['hi']), ['hi'])

    def test_multiple_element_lists(self):
        self.assertEqual(total_match(['hi', 'admin', 'project'], ['hI', 'Hi', 'HProject']), ['hi', 'admin'])
        self.assertEqual(total_match(['hi', 'admin', 'project', 'project'], ['hI', 'Hi', 'HProject', 'HProject']), ['hi', 'admin'])

if __name__ == '__main__':
    unittest.main()

This script tests the `total_match` function with various inputs, including:

* Empty lists
* Lists with the same length
* Lists where the first list is shorter
* Lists where the second list is shorter
* Lists where the first list is longer
* Lists with single elements
* Lists with multiple elements

Each test case checks that the output of the `total_match` function is as expected. If any of the tests fail, it will indicate a bug in the `total_match` function.