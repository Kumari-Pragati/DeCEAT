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
        return False

 Here is a unittest test script for the `is_sorted` function:


import unittest
from HumanEval_126_code import is_sorted

class TestIsSorted(unittest.TestCase):
    def test_is_sorted(self):
        self.assertTrue(is_sorted([5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5, 6, 7]))
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()


This test script includes a `TestIsSorted` class that contains several test cases for the `is_sorted` function. The `assertTrue` and `assertFalse` methods are used to verify that the function returns the expected results for the given test cases. The `unittest.main()` function is called at the end to run the tests.