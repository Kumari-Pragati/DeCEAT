You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_136_code import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(largest_smallest_integers([]), (None, None))

    def test_list_with_zero(self):
        self.assertEqual(largest_smallest_integers([0]), (None, None))

    def test_list_with_positive_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_list_with_negative_integers(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (None, None))

    def test_list_with_mixed_integers(self):
        self.assertEqual(largest_smallest_integers([-2, 4, -1, 3, 5, -7]), (-1, 3))

    def test_list_with_duplicates(self):
        self.assertEqual(largest_smallest_integers([-2, -2, -1, -1, 1, 1]), (-2, 1))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for empty list, list with zero, list with positive integers, list with negative integers, list with mixed integers, and list with duplicates. Each test checks if the function returns the correct tuple.