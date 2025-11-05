You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_151_code import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):

    def test_positive_odd_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([9, -2]), 81)

    def test_negative_numbers(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_zero(self):
        self.assertEqual(double_the_difference([0]), 0)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_non_integer_numbers(self):
        self.assertEqual(double_the_difference([1.5, 3.7, 2.2, 0.1]), 0)

    def test_non_positive_numbers(self):
        self.assertEqual(double_the_difference([-1, 0, 2]), 0)

    def test_even_numbers(self):
        self.assertEqual(double_the_difference([2, 4, 6]), 0)

if __name__ == '__main__':
    unittest.main()


This script tests the function with different types of inputs, including positive odd numbers, negative numbers, zero, an empty list, non-integer numbers, non-positive numbers, and even numbers. It checks that the function returns the correct output for each of these types of inputs.