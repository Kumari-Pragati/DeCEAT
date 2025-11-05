You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_generate_integers_with_valid_range(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
        self.assertEqual(generate_integers(10, 14), [])

    def test_generate_integers_with_lower_bound_less_than_2(self):
        self.assertEqual(generate_integers(1, 8), [2, 4, 6, 8])

    def test_generate_integers_with_upper_bound_greater_than_8(self):
        self.assertEqual(generate_integers(2, 10), [2, 4, 6, 8])

    def test_generate_integers_with_equal_boundaries(self):
        self.assertEqual(generate_integers(2, 2), [])

    def test_generate_integers_with_negative_numbers(self):
        self.assertEqual(generate_integers(-2, 8), [2, 4, 6, 8])
        self.assertEqual(generate_integers(8, -2), [2, 4, 6, 8])

    def test_generate_integers_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            generate_integers(2.5, 8)
        with self.assertRaises(TypeError):
            generate_integers(8, 2.5)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including:

- Testing the function with valid ranges where the lower bound is less than or equal to the upper bound.
- Testing the function with the lower bound greater than 2 and the upper bound less than or equal to 8.
- Testing the function with the lower bound greater than 8 and the upper bound less than or equal to 8.
- Testing the function with equal lower and upper bounds.
- Testing the function with negative numbers to ensure it handles them correctly.
- Testing the function with non-integer values to ensure it raises a `TypeError`.

Each test case checks the function's output against the expected result, ensuring that the function behaves as intended under different conditions.