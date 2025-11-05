user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_136_code import largest_smallest_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_136_code import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):

    def test_largest_smallest_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))
        self.assertEqual(largest_smallest_integers([-1, -2, -3, 1, 2, 3]), (-3, 1))
        self.assertEqual(largest_smallest_integers([-1, -2, -3, 0, 0, 0]), (-3, None))
        self.assertEqual(largest_smallest_integers([-1, -2, -3, 1, 2, 3, 4, 5, 6, 7]), (-3, 1))

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure the function is working correctly. The test cases cover various scenarios, including:

- A list with both negative and positive integers
- An empty list
- A list with only zeros
- A list with only negative integers
- A list with both negative and positive integers, and the smallest positive integer is zero

The `assertEqual` method is used to compare the expected output with the actual output of the function. If the actual output matches the expected output, the test case passes. If not, the test case fails and an error message is displayed.