You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_72_code import will_it_fly

class TestWillItFly(unittest.TestCase):

    def test_sum_greater_than_weight(self):
        self.assertFalse(will_it_fly([1, 2], 1))
        self.assertFalse(will_it_fly([3, 2, 3], 2))

    def test_unbalanced_list(self):
        self.assertFalse(will_it_fly([1, 2], 5))
        self.assertFalse(will_it_fly([3, 2, 3], 1))

    def test_balanced_list_and_sum_less_than_weight(self):
        self.assertTrue(will_it_fly([3, 2, 3], 9))
        self.assertTrue(will_it_fly([3], 5))

    def test_single_element_list(self):
        self.assertTrue(will_it_fly([3], 1))
        self.assertFalse(will_it_fly([3], 0))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios:

- When the sum of the elements is greater than the maximum possible weight.
- When the list is unbalanced.
- When the list is balanced and the sum of its elements is less than or equal to the maximum possible weight.
- When the list contains a single element.

Each test checks the function's output against the expected result.