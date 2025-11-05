user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the `is_sorted` function:

import unittest
from HumanEval_126_code import is_sorted

class TestIsSorted(unittest.TestCase):
    def test_single_element_list(self):
        self.assertTrue(is_sorted([5]))

    def test_ascending_list(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))

    def test_descending_list(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))

    def test_list_with_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))

    def test_list_with_multiple_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

    def test_empty_list(self):
        self.assertTrue(is_sorted([]))

    def test_list_with_one_duplicate(self):
        self.assertFalse(is_sorted([1, 2, 2, 3, 4]))

    def test_list_with_no_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))

    def test_list_with_no_duplicates_and_long(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))

    def test_list_with_duplicates_and_long(self):
        self.assertFalse(is_sorted([1, 2, 2, 3, 3, 4, 5, 6]))

if __name__ == '__main__':
    unittest.main()

This test script covers various scenarios, including:

* Single-element list
* Ascending list
* Descending list
* List with duplicates
* List with multiple duplicates
* Empty list
* List with one duplicate
* List with no duplicates and long
* List with duplicates and long

Each test method checks the output of the `is_sorted` function for a specific input, and asserts that the output is correct using the `assertTrue` or `assertFalse` methods.