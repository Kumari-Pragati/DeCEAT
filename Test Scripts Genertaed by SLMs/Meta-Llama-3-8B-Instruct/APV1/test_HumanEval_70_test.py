user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_strange_sort_list(self):
        # Test case 1: [1, 2, 3, 4]
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

        # Test case 2: [5, 5, 5, 5]
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

        # Test case 3: []
        self.assertEqual(strange_sort_list([]), [])

        # Test case 4: [1, 3, 2, 4]
        self.assertEqual(strange_sort_list([1, 3, 2, 4]), [1, 4, 2, 3])

        # Test case 5: [2, 1, 3, 4]
        self.assertEqual(strange_sort_list([2, 1, 3, 4]), [1, 4, 2, 3])

        # Test case 6: [1, 2, 3, 4, 5]
        self.assertEqual(strange_sort_list([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3])

        # Test case 7: [5, 4, 3, 2, 1]
        self.assertEqual(strange_sort_list([5, 4, 3, 2, 1]), [5, 1, 4, 3, 2])

        # Test case 8: [1, 1, 1, 1]
        self.assertEqual(strange_sort_list([1, 1, 1, 1]), [1, 1, 1, 1])

        # Test case 9: [2, 3, 4, 5, 6]
        self.assertEqual(strange_sort_list([2, 3, 4, 5, 6]), [2, 6, 3, 5, 4])

        # Test case 10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 10, 2, 9, 3, 8, 4, 7, 5, 6])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of test cases to ensure the function works correctly in different scenarios.