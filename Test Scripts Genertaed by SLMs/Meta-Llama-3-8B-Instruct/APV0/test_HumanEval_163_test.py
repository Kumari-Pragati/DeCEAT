user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_163_code import generate_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))
    return [i for i in range(lower, upper + 1) if i % 2 == 0]assistant

Here is the unittest test script for the `generate_integers` function:

import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):
    def test_generate_integers(self):
        # Test cases
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])
        self.assertEqual(generate_integers(1, 3), [])
        self.assertEqual(generate_integers(4, 6), [4, 6])
        self.assertEqual(generate_integers(6, 8), [6, 8])
        self.assertEqual(generate_integers(2, 2), [2])
        self.assertEqual(generate_integers(8, 8), [8])

    def test_edge_cases(self):
        # Test edge cases
        self.assertEqual(generate_integers(1, 1), [])
        self.assertEqual(generate_integers(2, 2), [2])
        self.assertEqual(generate_integers(8, 8), [8])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestGenerateIntegers` class with two test methods: `test_generate_integers` and `test_edge_cases`. The first method tests the main functionality of the `generate_integers` function with various input pairs, while the second method tests edge cases such as single-digit inputs, equal inputs, and identical inputs.

You can run this script directly to execute the tests and verify that the `generate_integers` function is working correctly.