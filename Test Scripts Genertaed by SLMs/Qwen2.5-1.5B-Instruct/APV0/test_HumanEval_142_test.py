system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
        elif i % 4 == 0 and i % 3 != 0:
            result.append(lst[i] ** 3)
        else:
            result.append(lst[i])
    return sum(result)


assistant

import unittest

# Importing the function to be tested
from HumanEval_142_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_sum_squares(self):
        # Test case 1
        self.assertEqual(sum_squares([1, 2, 3]), 6)
        
        # Test case 2
        self.assertEqual(sum_squares([]), 0)
        
        # Test case 3
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)
        
        # Test case 4 (Multiple of 3 but not 4)
        self.assertEqual(sum_squares([1, 2, 3, 4, 5]), 1 + 9 + 25 + 5)
        
        # Test case 5 (Multiple of 4 but not 3)
        self.assertEqual(sum_squares([1, 2, 3, 4, 5, 6]), 1 + 8 + 27 + 16 + 64 + 125)
        
        # Test case 6 (Multiple of both 3 and 4)
        self.assertEqual(sum_squares([1, 2, 3, 4, 5, 6, 7]), 1 + 9 + 25 + 16 + 64 + 125 + 49)
    
    def test_edge_cases(self):
        # Test empty list
        self.assertEqual(sum_squares([]), 0)
        
        # Test single element list
        self.assertEqual(sum_squares([1]), 1)
        
        # Test negative numbers
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)
        
        # Test mixed multiples of 3 and 4
        self.assertEqual(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100)

if __name__ == '__main__':
    unittest.main()


This script defines a `TestSumSquares` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `sum_squares` function under various conditions. The tests cover different scenarios including edge cases like an empty list, lists with single elements, lists containing negative numbers, and lists with mixed multiples of 3 and 4. The `unittest.main()` call at the end makes the script executable when run as a standalone program.