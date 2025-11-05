user

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
        elif i % 4 == 0 and i % 3!= 0:
            result.append(lst[i] ** 3)
        else:
            result.append(lst[i])
    return sum(result)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_142_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 6)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)
        self.assertEqual(sum_squares([1,2,3,4,5,6]), 36)
        self.assertEqual(sum_squares([1,2,3,4,5,6,7,8,9]), 100)
        self.assertEqual(sum_squares([1,2,3,4,5,6,7,8,9,10]), 145)

    def test_sum_squares_negative_numbers(self):
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)
        self.assertEqual(sum_squares([-1,-5,2,-1,-5,6,7,8,9,10]), -126)

    def test_sum_squares_zero(self):
        self.assertEqual(sum_squares([0,0,0,0,0,0,0,0,0,0]), 0)

    def test_sum_squares_single_element(self):
        self.assertEqual(sum_squares([1]), 1)
        self.assertEqual(sum_squares([-1]), -1)
        self.assertEqual(sum_squares([0]), 0)

    def test_sum_squares_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

if __name__ == '__main__':
    unittest.main()


This script includes tests for the following cases:
- Test with a list of integers
- Test with an empty list
- Test with negative numbers
- Test with zero
- Test with a single element
- Test with an empty list