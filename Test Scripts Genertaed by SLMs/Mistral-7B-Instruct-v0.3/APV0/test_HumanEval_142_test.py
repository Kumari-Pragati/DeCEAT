Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_142_code import sum_squares
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    result = []
    for i in range(len(lst)):
        if i % 3 == 0:
            result.append(lst[i] ** 2)
        elif i % 4 == 0 and i % 3 != 0:
            result.append(lst[i] ** 3)
        else:
            result.append(lst[i])
    return sum(result)

 Here is a unittest test script for the `sum_squares` function. The test cases cover the base cases and edge cases as specified in the function description.


import unittest
from HumanEval_142_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_single_element_list(self):
        self.assertEqual(sum_squares([1]), 1)

    def test_simple_list(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_list_with_3s(self):
        self.assertEqual(sum_squares([1, 2, 3, 4, 5, 6, 3, 9]), 16 + 3**3 + 9**3)

    def test_list_with_4s_not_3s(self):
        self.assertEqual(sum_squares([1, 2, 4, 5, 6, 8]), 1 + 2**2 + 4**3 + 5**2 + 6**2 + 8**3)

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_squares([-1, -2, 3, -4, 5, -6]), -1 + 3**2 + 4**3 + 5**2 + 6**2)

if __name__ == '__main__':
    unittest.main()


This test script includes six test cases covering different scenarios, such as an empty list, a single-element list, a simple list, a list with 3s, a list with 4s not being a multiple of 3, and a list with negative numbers. The test script will run these test cases when executed directly.