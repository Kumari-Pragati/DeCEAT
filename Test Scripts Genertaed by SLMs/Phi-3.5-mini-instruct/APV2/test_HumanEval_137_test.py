You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_137_code import compare_one
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    temp_a, temp_b = a, b
    if isinstance(temp_a, str):
        temp_a = temp_a.replace(',', '.')
    if isinstance(temp_b, str):
        temp_b = temp_b.replace(',', '.')
    if float(temp_a) == float(temp_b):
        return None
    return a if float(temp_a) > float(temp_b) else b

 import unittest
from HumanEval_137_code import compare_one

class TestCompareOne(unittest.TestCase):

    def test_compare_one_with_integers(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)

    def test_compare_one_with_floats(self):
        self.assertEqual(compare_one(1.0, 2.5), 2.5)

    def test_compare_one_with_strings_representing_floats(self):
        self.assertEqual(compare_one("1", "2.5"), "2.5")
        self.assertEqual(compare_one("2,5", "2.5"), "2.5")

    def test_compare_one_with_equal_values(self):
        self.assertIsNone(compare_one(1, 1))

    def test_compare_one_with_strings(self):
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertEqual(compare_one("5,1", "5,1"), None)

    def test_compare_one_with_mixed_types(self):
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", 6), 6)

    def test_compare_one_with_negative_values(self):
        self.assertEqual(compare_one(-1, -2.5), -1)

    def test_compare_one_with_zero(self):
        self.assertEqual(compare_one(0, 0), None)

if __name__ == '__main__':
    unittest.main()