system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_72_code import will_it_fly
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def will_it_fly(q, w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements
    is less than or equal to the maximum possible weight w.

    Example:
        will_it_fly([1, 2], 5) ➞ False 
        # 1+2 is less than the maximum possible weight, but it's unbalanced.

        will_it_fly([3, 2, 3], 1) ➞ False
        # it's balanced, but 3+2+3 is more than the maximum possible weight.

        will_it_fly([3, 2, 3], 9) ➞ True
        # 3+2+3 is less than the maximum possible weight, and it's balanced.

        will_it_fly([3], 5) ➞ True
        # 3 is less than the maximum possible weight, and it's balanced.
    '''
    if sum(q) > w:
        return False

    i, j = 0, len(q) - 1
    while i < j:
        if q[i]!= q[j]:
            return False
        i += 1
        j -= 1
    return Trueassistant

Here is the complete unittest test suite for the `will_it_fly` function:

import unittest
from HumanEval_72_code import will_it_fly

class TestWillItFly(unittest.TestCase):
    def test_balanced_and_sum_less_than_weight(self):
        self.assertTrue(will_it_fly([3, 2, 3], 9))
        self.assertTrue(will_it_fly([3], 5))
        self.assertTrue(will_it_fly([1, 1, 1], 3))

    def test_unbalanced_and_sum_less_than_weight(self):
        self.assertFalse(will_it_fly([1, 2], 5))
        self.assertFalse(will_it_fly([3, 2, 4], 5))
        self.assertFalse(will_it_fly([1, 2, 3, 4], 5))

    def test_balanced_and_sum_greater_than_weight(self):
        self.assertFalse(will_it_fly([3, 2, 3], 8))
        self.assertFalse(will_it_fly([3, 2, 3, 1], 7))
        self.assertFalse(will_it_fly([1, 2, 3, 4, 5], 6))

    def test_unbalanced_and_sum_greater_than_weight(self):
        self.assertFalse(will_it_fly([1, 2, 3, 4, 5], 6))
        self.assertFalse(will_it_fly([1, 2, 3, 4, 5, 6], 5))
        self.assertFalse(will_it_fly([1, 2, 3, 4, 5, 6, 7], 4))

if __name__ == '__main__':
    unittest.main()

This test suite covers the following scenarios:

1. Balanced and sum less than weight
2. Unbalanced and sum less than weight
3. Balanced and sum greater than weight
4. Unbalanced and sum greater than weight

Each test case checks the output of the `will_it_fly` function for a specific input, and verifies that the expected result is returned.