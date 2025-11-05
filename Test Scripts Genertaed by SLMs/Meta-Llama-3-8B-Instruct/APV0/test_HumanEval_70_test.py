user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_70_code import strange_sort_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
        strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
        strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
        strange_sort_list([]) == []
    '''
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return resassistant

Here is a unittest test script for the `strange_sort_list` function:

import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):
    def test_strange_sort_list(self):
        # Test 1: Simple case
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

        # Test 2: All equal elements
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

        # Test 3: Empty list
        self.assertEqual(strange_sort_list([]), [])

        # Test 4: Mixed elements
        self.assertEqual(strange_sort_list([3, 1, 4, 2, 5]), [1, 5, 2, 4, 3])

        # Test 5: Large list
        self.assertEqual(strange_sort_list([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
                         [10, 100, 20, 90, 30, 80, 40, 70, 50, 60])

    def test_edge_cases(self):
        # Test 6: Single element list
        self.assertEqual(strange_sort_list([5]), [5])

        # Test 7: List with duplicate elements
        self.assertEqual(strange_sort_list([1, 2, 2, 3, 3, 3]), [1, 3, 2, 3, 2, 3])

if __name__ == '__main__':
    unittest.main()

This script defines two test cases:

1. `test_strange_sort_list`: This test case checks the function with various input lists, including simple cases, all equal elements, empty list, mixed elements, and a large list.
2. `test_edge_cases`: This test case checks the function with edge cases, including a single element list and a list with duplicate elements.

You can run this script directly to execute the tests and verify that the `strange_sort_list` function is working correctly.