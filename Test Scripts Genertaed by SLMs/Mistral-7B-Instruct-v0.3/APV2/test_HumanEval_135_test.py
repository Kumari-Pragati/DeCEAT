You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_135_code import can_arrange
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    ind = -1
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            ind = i
        i += 1
    return ind

 Here is a complete unittest test suite for the `can_arrange` function:


import unittest
from HumanEval_135_code import can_arrange

class TestCanArrange(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(can_arrange([]), -1)

    def test_single_element(self):
        self.assertEqual(can_arrange([1]), -1)

    def test_increasing_sequence(self):
        self.assertEqual(can_arrange([1, 2, 3]), -1)

    def test_decreasing_sequence(self):
        self.assertEqual(can_arrange([5, 4, 3, 2, 1]), 4)

    def test_mixed_sequence(self):
        self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 3)

    def test_random_sequence(self):
        self.assertEqual(can_arrange([7, 6, 3, 4, 1, 5, 2]), 4)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, single element, increasing sequence, decreasing sequence, mixed sequence, and a random sequence. The test cases use the `assertEqual` method to compare the expected and actual output of the `can_arrange` function.