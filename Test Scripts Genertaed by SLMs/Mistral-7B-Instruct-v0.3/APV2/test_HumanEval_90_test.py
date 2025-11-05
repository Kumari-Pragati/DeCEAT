You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `next_smallest` function:


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

    def test_unique_elements_list(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 1)
        self.assertEqual(next_smallest([4, 2, 1, 3, 5]), 2)
        self.assertEqual(next_smallest([3, 2, 1, 4, 5]), 2)
        self.assertEqual(next_smallest([2, 1, 4, 3, 5]), 1)
        self.assertEqual(next_smallest([2, 1, 3, 4, 5]), None)

    def test_duplicate_elements_list(self):
        self.assertEqual(next_smallest([1, 1]), None)
        self.assertEqual(next_smallest([5, 5]), None)
        self.assertEqual(next_smallest([2, 2]), None)
        self.assertEqual(next_smallest([3, 3]), None)
        self.assertEqual(next_smallest([4, 4]), None)
        self.assertEqual(next_smallest([5, 5]), None)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different scenarios, such as empty lists, single-element lists, unique elements lists, duplicate elements lists, and lists with only one unique element. It uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.