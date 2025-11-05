user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_151_code import double_the_difference
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    return sum([i**2 for i in lst if i > 0 and i % 2!= 0 and "." not in str(i)])assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_151_code import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):

    def test_positive_odd_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_negative_numbers(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(double_the_difference([9, -2]), 81)

    def test_zero(self):
        self.assertEqual(double_the_difference([0]), 0)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_non_integer(self):
        self.assertEqual(double_the_difference([1.5, 3.5, 2.5, 0.5]), 0)

    def test_non_odd_numbers(self):
        self.assertEqual(double_the_difference([2, 4, 6, 8]), 0)

if __name__ == '__main__':
    unittest.main()


This script includes tests for the following scenarios:

1. A list with positive odd numbers.
2. A list with negative numbers.
3. A list with mixed numbers (positive and negative).
4. A list with zero.
5. An empty list.
6. A list with non-integer numbers.
7. A list with non-odd numbers.

Each test case checks if the output of the `double_the_difference` function matches the expected output.