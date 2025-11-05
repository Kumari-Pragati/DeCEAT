You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 
import unittest
from HumanEval_142_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_single_element_list(self):
        self.assertEqual(sum_squares([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_multiple_elements_list_with_negatives(self):
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

    def test_multiple_elements_list_with_positives(self):
        self.assertEqual(sum_squares([1, 2, 3, 4, 5]), 38)

    def test_multiple_elements_list_with_mixed_signs(self):
        self.assertEqual(sum_squares([-1, -2, 3, -4, 5]), -1)

    def test_multiple_elements_list_with_zero(self):
        self.assertEqual(sum_squares([0, 2, 0, 4, 0]), 24)

    def test_multiple_elements_list_with_large_numbers(self):
        self.assertEqual(sum_squares([100, 200, 300, 400, 500]), 350000)

    def test_multiple_elements_list_with_even_length(self):
        self.assertEqual(sum_squares([1, 2, 3, 4]), 30)

    def test_multiple_elements_list_with_odd_length(self):
        self.assertEqual(sum_squares([1, 2, 3, 4, 5]), 38)

    def test_multiple_elements_list_with_negative_index(self):
        self.assertEqual(sum_squares([1, 2, 3, 4, 5, -1]), 38)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios including empty lists, lists with single and multiple elements, lists with negative numbers, lists with mixed signs, lists with zeros, lists with large numbers, lists with even and odd lengths, and lists with negative indices. Each test case checks the output of the `sum_squares` function against the expected result.