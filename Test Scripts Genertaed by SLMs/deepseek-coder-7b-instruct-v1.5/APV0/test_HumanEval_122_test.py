You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_122_code import add_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):
    def test_add_elements(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)
        self.assertEqual(add_elements([10, 200, 3000, 40000, 500000], 3), 10)
        self.assertEqual(add_elements([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(add_elements([100, 2000, 30000, 400000, 5000000], 2), 300)
        self.assertEqual(add_elements([1000, 20000, 300000, 4000000, 50000000], 1), 1000)

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure that the `add_elements` function is working as expected. Each test case checks the function with a different input and verifies that the output matches the expected result.

Please note that you need to have the `HumanEval_122_code` module with the `add_elements` function defined in it for these tests to work.