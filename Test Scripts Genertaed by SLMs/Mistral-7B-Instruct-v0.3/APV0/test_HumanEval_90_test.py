Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a complete unittest test script for the `next_smallest` function:


import unittest
from HumanEval_90_code import next_smallest

class TestNextSmallest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(next_smallest([]), None)

    def test_single_element_list(self):
        self.assertEqual(next_smallest([1]), None)
        self.assertEqual(next_smallest([5]), None)

    def test_single_unique_element_list(self):
        self.assertEqual(next_smallest([1]), None)
        self.assertEqual(next_smallest([5]), None)

    def test_duplicate_single_element_list(self):
        self.assertEqual(next_smallest([1, 1]), None)

    def test_single_element_at_index_0(self):
        self.assertEqual(next_smallest([0]), None)

    def test_multiple_elements(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 1)
        self.assertEqual(next_smallest([4, 2, 1, 3, 5]), 1)
        self.assertEqual(next_smallest([3, 2, 1]), 1)
        self.assertEqual(next_smallest([2, 1]), None)

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to cover different scenarios, such as an empty list, a single-element list, multiple elements, and edge cases like when the smallest element is at index 0 or when there are duplicates.