You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers_positive(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])
        self.assertEqual(generate_integers(1, 1), [])
        self.assertEqual(generate_integers(8, 8), [8])

    def test_generate_integers_negative(self):
        self.assertEqual(generate_integers(-2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, -2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(-8, -2), [])
        self.assertEqual(generate_integers(-10, -14), [])
        self.assertEqual(generate_integers(-1, -1), [])
        self.assertEqual(generate_integers(-8, -8), [-8])

    def test_generate_integers_boundary(self):
        self.assertEqual(generate_integers(0, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 0), [2, 4, 6, 8])
        self.assertEqual(generate_integers(0, 0), [])
        self.assertEqual(generate_integers(-2, 0), [0, 2, 4, 6, 8])
        self.assertEqual(generate_integers(0, 2), [0, 2])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, negative numbers, and boundary cases. It checks if the function returns the correct list of even integers between the given two numbers, regardless of their signs or whether they are in ascending or descending order.