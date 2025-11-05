user

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
        return lst2assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_74_code import total_match

class TestTotalMatch(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])

    def test_lists_with_same_chars(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'admin']), ['hi', 'admin'])

    def test_list1_has_less_chars(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_list2_has_less_chars(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_lists_with_mixed_case(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_list_with_single_element(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

    def test_lists_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            total_match([1, 2], ['a', 'b'])

    def test_lists_with_mixed_types(self):
        with self.assertRaises(TypeError):
            total_match([1, 'a'], ['b', 'c'])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including:

- Testing with empty lists
- Testing with lists that have the same number of characters
- Testing with lists where one list has less characters than the other
- Testing with lists that contain mixed case strings
- Testing with lists that contain single elements
- Testing with lists that contain non-string elements
- Testing with lists that contain mixed types