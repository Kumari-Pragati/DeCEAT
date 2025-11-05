Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_83_code import starts_one_ends
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))

 Here is a unittest test script for the `starts_one_ends` function:


import unittest
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):
    def test_starts_one_ends(self):
        self.assertEqual(starts_one_ends(1), 1)
        self.assertEqual(starts_one_ends(2), 18)
        self.assertEqual(starts_one_ends(3), 180)
        self.assertEqual(starts_one_ends(4), 1800)
        self.assertEqual(starts_one_ends(5), 18000)
        self.assertEqual(starts_one_ends(6), 180000)
        self.assertEqual(starts_one_ends(7), 1800000)
        self.assertEqual(starts_one_ends(8), 18000000)
        self.assertEqual(starts_one_ends(9), 180000000)
        self.assertEqual(starts_one_ends(10), 1800000000)

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `starts_one_ends` function with different input values ranging from 1 to 10. The test case uses the `assertEqual` method to check if the output of the function matches the expected output.