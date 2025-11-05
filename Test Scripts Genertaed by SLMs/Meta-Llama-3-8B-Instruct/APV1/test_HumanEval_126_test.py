user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_126_code import is_sorted
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i] += 1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i - 1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return Falseassistant

Here is the comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_126_code import is_sorted

class TestIsSorted(unittest.TestCase):

    def test_single_element_list(self):
        self.assertTrue(is_sorted([5]))

    def test_ascending_order_list(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))

    def test_descending_order_list(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))

    def test_list_with_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))

    def test_list_with_duplicates_and_descending_order(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

    def test_empty_list(self):
        self.assertTrue(is_sorted([]))

    def test_list_with_single_duplicate(self):
        self.assertFalse(is_sorted([1, 2, 2, 3, 4]))

    def test_list_with_multiple_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 3, 4]))

    def test_list_with_duplicates_and_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 3, 3, 4]))

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of test cases, including:

* Single-element lists
* Ascending and descending order lists
* Lists with duplicates
* Empty lists
* Lists with single and multiple duplicates
* Lists with duplicates and duplicates

Each test case is designed to test a specific aspect of the `is_sorted` function, and the test suite as a whole provides comprehensive coverage of the function's behavior.