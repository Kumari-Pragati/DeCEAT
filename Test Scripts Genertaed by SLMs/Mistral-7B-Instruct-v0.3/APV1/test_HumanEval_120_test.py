You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return ans

 Here is a comprehensive unittest test suite for the given Python function `maximum`.


import unittest
from HumanEval_120_code import maximum

class TestMaximum(unittest.TestCase):

    def test_example_1(self):
        self.assertListEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_example_2(self):
        self.assertListEqual(maximum([4, -4, 4], 2), [4, 4])

    def test_example_3(self):
        self.assertListEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    def test_empty_array(self):
        self.assertListEqual(maximum([], 3), [])

    def test_single_element(self):
        self.assertListEqual(maximum([1], 1), [1])

    def test_k_greater_than_array_length(self):
        self.assertListEqual(maximum([1, 2, 3], 4), [3, 2, 1])

    def test_negative_k(self):
        self.assertListEqual(maximum([1, 2, 3], -1), [])

    def test_k_zero(self):
        self.assertListEqual(maximum([-3, -4, 5], 0), [])

    def test_negative_numbers(self):
        self.assertListEqual(maximum([-3, -4, -5], 3), [-5, -4, -3])

    def test_positive_numbers(self):
        self.assertListEqual(maximum([5, 4, 3], 3), [5, 4, 3])

    def test_mixed_numbers(self):
        self.assertListEqual(maximum([-3, 5, -4, 4], 3), [5, 4, -4])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as:

1. Different examples provided in the function description
2. Empty array
3. Single-element array
4. k greater than array length
5. k equal to 0
6. Negative k
7. Array with only negative numbers
8. Array with only positive numbers
9. Array with mixed numbers

It uses the `assertListEqual` method to compare the expected output with the actual output returned by the `maximum` function.