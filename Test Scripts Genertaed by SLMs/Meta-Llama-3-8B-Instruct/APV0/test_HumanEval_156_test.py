user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return res.lower()assistant

Here is the unittest test script for the `int_to_mini_roman` function:

import unittest
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(4), 'iv')
        self.assertEqual(int_to_mini_roman(5), 'v')
        self.assertEqual(int_to_mini_roman(9), 'ix')
        self.assertEqual(int_to_mini_roman(10), 'x')
        self.assertEqual(int_to_mini_roman(40), 'xl')
        self.assertEqual(int_to_mini_roman(50), 'l')
        self.assertEqual(int_to_mini_roman(90), 'xc')
        self.assertEqual(int_to_mini_roman(100), 'c')
        self.assertEqual(int_to_mini_roman(400), 'cd')
        self.assertEqual(int_to_mini_roman(500), 'd')
        self.assertEqual(int_to_mini_roman(900), 'cm')
        self.assertEqual(int_to_mini_roman(1000),'m')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            int_to_mini_roman(0)
        with self.assertRaises(ValueError):
            int_to_mini_roman(1001)

    def test_edge_cases(self):
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(4), 'iv')
        self.assertEqual(int_to_mini_roman(5), 'v')
        self.assertEqual(int_to_mini_roman(9), 'ix')
        self.assertEqual(int_to_mini_roman(10), 'x')
        self.assertEqual(int_to_mini_roman(40), 'xl')
        self.assertEqual(int_to_mini_roman(50), 'l')
        self.assertEqual(int_to_mini_roman(90), 'xc')
        self.assertEqual(int_to_mini_roman(100), 'c')
        self.assertEqual(int_to_mini_roman(400), 'cd')
        self.assertEqual(int_to_mini_roman(500), 'd')
        self.assertEqual(int_to_mini_roman(900), 'cm')
        self.assertEqual(int_to_mini_roman(1000),'m')

if __name__ == '__main__':
    unittest.main()

This test script includes three test cases:

1. `test_valid_input`: Tests the function with valid input values (1-1000) and checks that the output is correct.
2. `test_invalid_input`: Tests the function with invalid input values (0 and 1001) and checks that it raises a `ValueError`.
3. `test_edge_cases`: Tests the function with edge cases (1-1000) and checks that the output is correct.

Note that this test script assumes that the `int_to_mini_roman` function is defined in the `HumanEval_156_code` module. If the function is defined elsewhere, you'll need to modify the import statement accordingly.