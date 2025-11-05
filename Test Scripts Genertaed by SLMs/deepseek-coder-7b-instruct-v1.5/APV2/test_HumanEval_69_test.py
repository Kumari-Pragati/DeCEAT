You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_69_code import search

class TestSearch(unittest.TestCase):

    def test_search(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)
        self.assertEqual(search([1, 1, 1, 1, 1]), 1)
        self.assertEqual(search([2, 2, 2, 2, 2]), -1)
        self.assertEqual(search([3, 3, 3, 3, 3, 2, 2, 2]), 3)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9]), -1)
        self.assertEqual(search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the `search` function is working correctly. It tests with a variety of input lists, including ones where the answer is 1, -1, or a number greater than 1.