You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    def test_generate_integers_with_even_range(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_generate_integers_with_odd_range(self):
        self.assertEqual(generate_integers(1, 5), [])

    def test_generate_integers_with_lower_even(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_generate_integers_with_upper_even(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_generate_integers_with_equal_values(self):
        self.assertEqual(generate_integers(2, 2), [2])

    def test_generate_integers_with_lower_odd(self):
        self.assertEqual(generate_integers(3, 5), [])

    def test_generate_integers_with_upper_odd(self):
        self.assertEqual(generate_integers(5, 3), [])

    def test_generate_integers_with_lower_out_of_range(self):
        self.assertEqual(generate_integers(0, 8), [2, 4, 6, 8])

    def test_generate_integers_with_upper_out_of_range(self):
        self.assertEqual(generate_integers(8, 0), [2, 4, 6, 8])

    def test_generate_integers_with_negative_values(self):
        self.assertEqual(generate_integers(-2, 8), [2, 4, 6, 8])

    def test_generate_integers_with_zero_values(self):
        self.assertEqual(generate_integers(0, 8), [2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()