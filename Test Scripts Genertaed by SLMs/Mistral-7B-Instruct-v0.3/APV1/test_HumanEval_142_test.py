You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `sum_squares`. I have included various test cases to cover different scenarios:


import unittest
from HumanEval_142_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_single_element_list(self):
        self.assertEqual(sum_squares([1]), 1)

    def test_simple_list(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_list_with_multiple_of_3(self):
        self.assertEqual(sum_squares([1, 3, 2, 3, 4]), 14)

    def test_list_with_multiple_of_4_not_3(self):
        self.assertEqual(sum_squares([1, 4, 2, 4, 5]), 108)

    def test_list_with_multiple_of_both_3_and_4(self):
        self.assertEqual(sum_squares([1, 3, 4, 2, 3, 4]), 149)

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

    def test_list_with_duplicates(self):
        self.assertEqual(sum_squares([1, 1, 3, 2, 3, 3]), 22)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios such as an empty list, single-element list, lists with multiple of 3, lists with multiple of 4 not multiple of 3, lists with multiple of both 3 and 4, lists with negative numbers, and lists with duplicates.