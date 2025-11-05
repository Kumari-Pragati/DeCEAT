You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 
import unittest
from HumanEval_151_code import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):

    def test_positive_odd_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_negative_numbers(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(double_the_difference([9, -2]), 81)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_non_integer_values(self):
        self.assertEqual(double_the_difference([1.5, 3, 2, 0]), 0)

    def test_zero_list(self):
        self.assertEqual(double_the_difference([0, 0, 0]), 0)

    def test_single_odd_number(self):
        self.assertEqual(double_the_difference([5]), 25)

    def test_no_odd_numbers(self):
        self.assertEqual(double_the_difference([2, 4, 6]), 0)

    def test_all_odd_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 5, 7]), 74)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including lists with positive and negative odd numbers, empty lists, lists with non-integer values, lists with zero values, lists with a single odd number, and lists with only even numbers. Each test case checks the expected output against the actual output from the `double_the_difference` function.