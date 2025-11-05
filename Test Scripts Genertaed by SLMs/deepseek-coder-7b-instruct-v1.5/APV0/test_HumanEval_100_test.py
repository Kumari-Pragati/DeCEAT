You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_100_code import make_a_pile
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """

    return [n + 2*i for i in range(n)]


### Response:
Here is the unittest script for the given Python function:


import unittest
from HumanEval_100_code import make_a_pile

class TestMakeAPile(unittest.TestCase):
    def test_make_a_pile_positive(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(1), [1])
        self.assertEqual(make_a_pile(0), [])
        self.assertEqual(make_a_pile(10), [10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_make_a_pile_negative(self):
        self.assertEqual(make_a_pile(-3), [])
        self.assertEqual(make_a_pile(-1), [])

    def test_make_a_pile_zero(self):
        self.assertEqual(make_a_pile(0), [])

if __name__ == '__main__':
    unittest.main()


This script includes three test methods:

- `test_make_a_pile_positive`: This method tests the function with positive integers.
- `test_make_a_pile_negative`: This method tests the function with negative integers.
- `test_make_a_pile_zero`: This method tests the function with zero.

Each method uses the `assertEqual` function to compare the output of the function with the expected output. If the function is working correctly, none of these tests should fail.

Please note that you need to replace `from HumanEval_100_code import make_a_pile` with the actual location of your function if it's not in the same file.