You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return res


### Response:
Here is a unittest script for the strange_sort_list function:


import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(strange_sort_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(strange_sort_list([1]), [1])

    def test_two_elements_list(self):
        self.assertEqual(strange_sort_list([1, 2]), [1, 2])
        self.assertEqual(strange_sort_list([2, 1]), [1, 2])

    def test_multiple_elements_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class TestStrangeSortList with several test methods to test the strange_sort_list function with different types of input. Each test method asserts that the output of the function matches the expected output for a given input.

Please note that the function is tested with empty list, list with single element, list with two elements, and list with multiple elements.

This script should be runnable directly as it is, as it includes the unittest module and the strange_sort_list function from the HumanEval_70_code module.

If the HumanEval_70_code module is not available or the strange_sort_list function is not defined in it, you need to define it or replace it with the correct function.