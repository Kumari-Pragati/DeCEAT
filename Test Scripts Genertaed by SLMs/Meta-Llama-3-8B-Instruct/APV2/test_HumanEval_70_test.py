system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the `strange_sort_list` function:


import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_strange_sort_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([]), [])
        self.assertEqual(strange_sort_list([1, 3, 2, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 2, 8, 3, 1, 4, 6, 7]), [1, 8, 2, 7, 3, 6, 4, 5])
        self.assertEqual(strange_sort_list([10, 20, 30, 40, 50]), [10, 50, 20, 40, 30])

if __name__ == '__main__':
    unittest.main()