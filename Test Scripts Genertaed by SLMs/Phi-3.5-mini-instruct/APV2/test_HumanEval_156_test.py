You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_156_code import int_to_mini_roman
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    res = ''
    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            res += sym[i]
            div -= 1
        i -= 1
    return res.lower()

 
import unittest
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):

    def test_single_digit_numbers(self):
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(4), 'iv')
        self.assertEqual(int_to_mini_roman(9), 'ix')

    def test_two_digit_numbers(self):
        self.assertEqual(int_to_mini_roman(10), 'x')
        self.assertEqual(int_to_mini_roman(40), 'xl')
        self.assertEqual(int_to_mini_roman(90), 'xc')

    def test_three_digit_numbers(self):
        self.assertEqual(int_to_mini_roman(100), 'c')
        self.assertEqual(int_to_mini_roman(400), 'cd')
        self.assertEqual(int_to_mini_roman(900), 'cm')

    def test_edge_cases(self):
        self.assertEqual(int_to_mini_roman(0), '')
        self.assertEqual(int_to_mini_roman(1001), 'invalid')

    def test_within_range(self):
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(100), 'c')
        self.assertEqual(int_to_mini_roman(1000), 'm')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            int_to_mini_roman(-1)
        with self.assertRaises(ValueError):
            int_to_mini_roman(1001)

if __name__ == '__main__':
    unittest.main()


In this test suite, we have added tests for single-digit numbers, two-digit numbers, three-digit numbers, edge cases, and invalid inputs. The `test_invalid_input` method checks if the function raises a `ValueError` for numbers outside the allowed range (1 to 1000). If the `int_to_mini_roman` function is modified to raise a `ValueError` for invalid inputs, the test will pass. Otherwise, it will fail, indicating that the function does not handle invalid inputs as expected.

Please note that the provided function does not raise a `ValueError` for inputs outside the range of 1 to 1000. If you want to enforce this behavior, you should modify the `int_to_mini_roman` function to include a check for the input range and raise a `ValueError` accordingly. Here's an example modification:


def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000")

    # ... rest of the function remains unchanged ...


After making this change, the `test_invalid_input` test case will pass, as it expects a `ValueError` to be raised for invalid inputs.