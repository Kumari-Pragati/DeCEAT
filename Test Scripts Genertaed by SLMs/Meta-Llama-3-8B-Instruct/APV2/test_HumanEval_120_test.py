system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_120_code import maximum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ansassistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_120_code import maximum

class TestMaximum(unittest.TestCase):

    def test_maximum(self):
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])
        self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])
        self.assertEqual(maximum([1, 2, 3, 4, 5], 3), [5, 4, 3])
        self.assertEqual(maximum([-1, -2, -3, -4, -5], 3), [-1, -2, -3])
        self.assertEqual(maximum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), [10, 9, 8, 7, 6])
        self.assertEqual(maximum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 5), [-1, -2, -3, -4, -5])
        self.assertEqual(maximum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15, ), [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(maximum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15], 15, ), [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])

    def test_zero_k(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 0), [])

    def test_k_greater_than_length(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 10), [5, 4, 3, 2, 1])

    def test_k_equal_to_length(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_k_equal_to_one(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 1), [5])

    def test_k_equal_to_length_of_array(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_k_equal_to_zero(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 0), [])

    def test_k_greater_than_length_of_array(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 10), [5, 4, 3, 2, 1])

    def test_k_equal_to_length_of_array(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_k_equal_to_zero(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 0), [])

    def test_k_greater_than_length_of_array(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 10), [5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()