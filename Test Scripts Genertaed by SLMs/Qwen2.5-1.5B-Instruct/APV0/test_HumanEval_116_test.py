system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_116_code import sort_array
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


assistant

import unittest

# Function to be tested
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):
    def test_sort_array(self):
        # Test case 1
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        
        # Test case 2
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        
        # Test case 3
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()


This script defines a `TestSortArray` class that inherits from `unittest.TestCase`. Each method within this class is a test case that uses assertions to verify if the `sort_array` function behaves as expected under different scenarios. The `assertEqual` method checks if two lists are equal, which helps ensure that the output matches the expected results.