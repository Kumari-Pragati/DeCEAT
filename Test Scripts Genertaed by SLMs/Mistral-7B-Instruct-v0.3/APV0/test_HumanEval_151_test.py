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
    return sum([i**2 for i in lst if i > 0 and i % 2 != 0 and "." not in str(i)])

 Here is a unittest test script for the `double_the_difference` function:


import unittest
from HumanEval_151_code import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_single_element(self):
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([1]), 1)
        self.assertEqual(double_the_difference([-1]), 0)

    def test_multiple_elements(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)

    def test_negative_numbers(self):
        self.assertEqual(double_the_difference([-1, 3, -2, 0]), 9)

    def test_floating_point_numbers(self):
        self.assertEqual(double_the_difference([1.5, 3, -2.5]), 9)

    def test_mixed_data_types(self):
        self.assertEqual(double_the_difference([1, "three", 3, -2]), 9)

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to cover different scenarios, such as an empty list, single elements, multiple elements, negative numbers, floating-point numbers, and mixed data types. It uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.