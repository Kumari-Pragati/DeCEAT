You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return [i for i in range(lower, upper + 1) if i % 2 == 0]

 Here is a complete unittest test suite for the `generate_integers` function:


import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers_basic(self):
        self.assertListEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertListEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertListEqual(generate_integers(10, 14), [])
        self.assertListEqual(generate_integers(1, 1), [])
        self.assertListEqual(generate_integers(1, 2), [2])
        self.assertListEqual(generate_integers(2, 1), [])
        self.assertListEqual(generate_integers(1, 3), [2])
        self.assertListEqual(generate_integers(3, 1), [])

    def test_generate_integers_edge_cases(self):
        self.assertListEqual(generate_integers(0, 2), [])
        self.assertListEqual(generate_integers(2, 0), [])
        self.assertListEqual(generate_integers(-1, 2), [])
        self.assertListEqual(generate_integers(2, -1), [])
        self.assertListEqual(generate_integers(2, 2), [2])
        self.assertListEqual(generate_integers(8, 8), [8])
        self.assertListEqual(generate_integers(8, 9), [8])
        self.assertListEqual(generate_integers(9, 8), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, including edge cases, and uses the `assertListEqual` method to verify the expected output. The test suite is named `TestGenerateIntegers` and inherits from `unittest.TestCase`.