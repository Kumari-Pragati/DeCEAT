You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    return res


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(strange_sort_list([]), [])

    def test_single_element(self):
        self.assertEqual(strange_sort_list([5]), [5])

    def test_two_elements(self):
        self.assertEqual(strange_sort_list([1, 2]), [1, 2])
        self.assertEqual(strange_sort_list([2, 1]), [1, 2])

    def test_multiple_elements(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([1, 3, 5, 7]), [1, 7, 3, 5])
        self.assertEqual(strange_sort_list([2, 2, 2, 2]), [2, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()


This suite includes tests for empty lists, single-element lists, two-element lists, and lists with multiple elements. It checks that the function returns the correct output for each of these cases.