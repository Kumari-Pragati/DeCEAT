system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_146_code import specialFilter
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
    return count


assistant

import unittest

# Function to be tested
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):
    def test_specialFilter(self):
        # Test case 1
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        
        # Test case 2
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
        
        # Test case 3
        self.assertEqual(specialFilter([-1, 98, 123, 456, 789]), 0)
        
        # Test case 4
        self.assertEqual(specialFilter([]), 0)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a test class `TestSpecialFilter` within it. Each method in this class is a test case that uses assertions to check whether the output of the `specialFilter` function matches the expected result. The `assertEqual` method compares two values and raises an AssertionError if they are not equal. If all tests pass without raising any assertion errors, the program will run successfully.