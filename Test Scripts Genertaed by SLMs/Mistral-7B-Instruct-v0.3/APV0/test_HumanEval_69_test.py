Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_69_code import search
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such value exists, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i

    return ans

 Here is a unittest test script for the provided function `search`. I have included several test cases to cover various scenarios.


import unittest
from HumanEval_69_code import search

class TestSearchFunction(unittest.TestCase):

    def test_search_simple(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_search_multiple_occurrences(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_search_only_one(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    def test_search_single_element(self):
        self.assertEqual(search([1]), -1)

    def test_search_no_greater_than_zero(self):
        self.assertEqual(search([0, 0, 0]), -1)

    def test_search_all_zero(self):
        self.assertEqual(search([0]), -1)

    def test_search_negative_numbers(self):
        self.assertEqual(search([-1, -2, -3]), -1)

    def test_search_multiple_occurrences_negative(self):
        self.assertEqual(search([-1, -2, -2, -3, -3, -3]), -1)

if __name__ == '__main__':
    unittest.main()


This test script includes test cases for various scenarios such as simple lists, multiple occurrences, only one element, no greater than zero, all zero, negative numbers, and multiple occurrences of negative numbers.