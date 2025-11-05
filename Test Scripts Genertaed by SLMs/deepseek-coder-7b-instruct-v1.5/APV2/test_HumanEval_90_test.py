You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_90_code import next_smallest
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_90_code import next_smallest

class TestNextSmallest(unittest.TestCase):

    def test_next_smallest_with_valid_input(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

    def test_next_smallest_with_empty_list(self):
        self.assertIsNone(next_smallest([]))

    def test_next_smallest_with_single_element(self):
        self.assertIsNone(next_smallest([1]))

    def test_next_smallest_with_duplicate_elements(self):
        self.assertIsNone(next_smallest([1, 1]))

    def test_next_smallest_with_duplicate_elements_and_zero(self):
        self.assertEqual(next_smallest([0, 0, 1]), 0)

    def test_next_smallest_with_negative_numbers(self):
        self.assertEqual(next_smallest([-1, -2, -3, -4, -5]), -2)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios including valid input, empty list, single element, duplicate elements, duplicate elements with zero, and negative numbers.