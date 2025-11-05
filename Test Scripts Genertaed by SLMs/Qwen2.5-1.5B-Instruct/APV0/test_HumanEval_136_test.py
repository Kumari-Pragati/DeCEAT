system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return (max(smallest) if smallest else None, min(largest) if largest else None)


assistant

import unittest

# Importing the function to be tested
from HumanEval_136_code import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):

    def test_largest_smallest_integers(self):
        # Test case 1: List contains both negative and positive numbers
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), ((-1,), 1))

        # Test case 2: List contains only negative numbers
        self.assertEqual(largest_smallest_integers([-5, -8, -9]), (None, None))

        # Test case 3: List contains only positive numbers
        self.assertEqual(largest_smallest_integers([1, 2, 3, 4, 5]), ((-1,), 1))

        # Test case 4: Empty list
        self.assertEqual(largest_smallest_integers([]), (None, None))

        # Test case 5: List contains only zero
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()


This script defines a `TestLargestSmallestIntegers` class within the `unittest` module, which inherits from `unittest.TestCase`. It includes several test cases using assertEqual methods to verify the correctness of the `largest_smallest_integers` function against various inputs. The `if __name__ == '__main__':` block ensures that the tests can be run directly when the script is executed.