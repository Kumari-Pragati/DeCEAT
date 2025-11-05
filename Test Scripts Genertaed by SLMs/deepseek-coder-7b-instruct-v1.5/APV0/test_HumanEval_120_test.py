You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_120_code import maximum

class TestMaximum(unittest.TestCase):

    def test_maximum_positive(self):
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])
        self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    def test_maximum_zero(self):
        self.assertEqual(maximum([], 0), [])

    def test_maximum_negative(self):
        self.assertEqual(maximum([-3, -4, 5], 0), [])
        self.assertEqual(maximum([], 3), [])

    def test_maximum_edge(self):
        self.assertEqual(maximum([1000]*1000, 1000), [1000]*1000)
        self.assertEqual(maximum([-1000]*1000, 1000), [-1000]*1000)

if __name__ == '__main__':
    unittest.main()


This script includes 4 test cases:

1. `test_maximum_positive`: tests the function with positive numbers and k greater than 0.
2. `test_maximum_zero`: tests the function with k equals to 0.
3. `test_maximum_negative`: tests the function with negative numbers and k equals to 0.
4. `test_maximum_edge`: tests the function with maximum and minimum numbers and with k equals to the length of the array.

To run this script, you need to have the function `maximum` defined in the file `HumanEval_120_code.py`.