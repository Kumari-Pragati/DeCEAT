You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
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


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(5), 'v')
        self.assertEqual(int_to_mini_roman(10), 'x')
        self.assertEqual(int_to_mini_roman(50), 'l')
        self.assertEqual(int_to_mini_roman(100), 'c')
        self.assertEqual(int_to_mini_roman(500), 'd')
        self.assertEqual(int_to_mini_roman(1000), 'm')

    def test_double_digit(self):
        self.assertEqual(int_to_mini_roman(2), 'ii')
        self.assertEqual(int_to_mini_roman(3), 'iii')
        self.assertEqual(int_to_mini_roman(6), 'vi')
        self.assertEqual(int_to_mini_roman(7), 'vii')
        self.assertEqual(int_to_mini_roman(8), 'viii')
        self.assertEqual(int_to_mini_roman(9), 'ix')
        self.assertEqual(int_to_mini_roman(11), 'xi')
        self.assertEqual(int_to_mini_roman(12), 'xii')
        self.assertEqual(int_to_mini_roman(15), 'xv')
        self.assertEqual(int_to_mini_roman(16), 'xvi')
        self.assertEqual(int_to_mini_roman(17), 'xvii')
        self.assertEqual(int_to_mini_roman(18), 'xviii')
        self.assertEqual(int_to_mini_roman(20), 'xx')

    def test_triple_digit(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(20), 'xx')
        self.assertEqual(int_to_mini_roman(21), 'xxi')
        self.assertEqual(int_to_mini_roman(30), 'xxx')
        self.assertEqual(int_to_mini_roman(40), 'xl')
        self.assertEqual(int_to_mini_roman(50), 'l')
        self.assertEqual(int_to_mini_roman(60), 'lx')
        self.assertEqual(int_to_mini_roman(70), 'lxx')
        self.assertEqual(int_to_mini_roman(80), 'lxxx')
        self.assertEqual(int_to_mini_roman(90), 'xc')
        self.assertEqual(int_to_mini_roman(100), 'c')

    def test_four_digit(self):
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')
        self.assertEqual(int_to_mini_roman(526), 'dxxvi')
        self.assertEqual(int_to_mini_roman(626), 'dcxxvi')
        self.assertEqual(int_to_mini_roman(726), 'dccxxvi')
        self.assertEqual(int_to_mini_roman(826), 'dcccxxvi')
        self.assertEqual(int_to_mini_roman(926), 'cmxxvi')

    def test_boundary_cases(self):
        self.assertEqual(int_to_mini_roman(1000), 'm')
        self.assertEqual(int_to_mini_roman(999), 'cmxcix')
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(0), '')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for single-digit numbers, double-digit numbers, triple-digit numbers, four-digit numbers, and boundary cases.