user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_136_code import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):

    def test_largest_smallest_integers_positive(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_largest_smallest_integers_negative(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (-7, None))

    def test_largest_smallest_integers_mixed(self):
        self.assertEqual(largest_smallest_integers([-2, 4, -1, 3, -5, 7]), (-5, 1))

    def test_largest_smallest_integers_no_negative(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_largest_smallest_integers_no_positive(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (-7, None))

    def test_largest_smallest_integers_no_integers(self):
        self.assertEqual(largest_smallest_integers([0, 0, 0]), (None, None))

    def test_largest_smallest_integers_empty_list(self):
        self.assertEqual(largest_smallest_integers([]), (None, None))

if __name__ == '__main__':
    unittest.main()


This test suite covers all the edge cases and examples provided in the problem description. It tests the function with positive integers, negative integers, mixed integers, no negative integers, no positive integers, no integers, and an empty list.