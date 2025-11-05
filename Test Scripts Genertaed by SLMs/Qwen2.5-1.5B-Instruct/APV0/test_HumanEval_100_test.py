system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Importing the function we want to test
from HumanEval_100_code import make_a_pile

class TestMakeAPile(unittest.TestCase):

    def test_make_a_pile(self):
        # Test case 1: n = 3
        self.assertEqual(make_a_pile(3), [3, 5, 7])

        # Test case 2: n = 4
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])

        # Test case 3: n = 5
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])

        # Test case 4: n = 6
        self.assertEqual(make_a_pile(6), [6, 8, 10, 12, 14, 16])

        # Test case 5: n = 7
        self.assertEqual(make_a_pile(7), [7, 9, 11, 13, 15, 17, 19])

        # Test case 6: n = 8
        self.assertEqual(make_a_pile(8), [8, 10, 12, 14, 16, 18, 20, 22])

if __name__ == '__main__':
    unittest.main()


This script defines a `TestMakeAPile` class that inherits from `unittest.TestCase`. It contains six test cases using the `assertEqual` method to verify that the output of `make_a_pile` matches the expected results. Finally, it calls `unittest.main()` to run all tests when the script is executed directly.