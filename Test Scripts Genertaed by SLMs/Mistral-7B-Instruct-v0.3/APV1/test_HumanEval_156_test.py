You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `int_to_mini_roman`.


import unittest
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):

    def test_int_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(1), 'i')
        self.assertEqual(int_to_mini_roman(2), 'ii')
        self.assertEqual(int_to_mini_roman(3), 'iii')
        self.assertEqual(int_to_mini_roman(4), 'iv')
        self.assertEqual(int_to_mini_roman(5), 'v')
        self.assertEqual(int_to_mini_roman(6), 'vi')
        self.assertEqual(int_to_mini_roman(7), 'vii')
        self.assertEqual(int_to_mini_roman(8), 'viii')
        self.assertEqual(int_to_mini_roman(9), 'ix')
        self.assertEqual(int_to_mini_roman(10), 'x')
        self.assertEqual(int_to_mini_roman(11), 'xi')
        self.assertEqual(int_to_mini_roman(12), 'xii')
        self.assertEqual(int_to_mini_roman(13), 'xiii')
        self.assertEqual(int_to_mini_roman(14), 'xiv')
        self.assertEqual(int_to_mini_roman(15), 'xv')
        self.assertEqual(int_to_mini_roman(16), 'xvi')
        self.assertEqual(int_to_mini_roman(17), 'xvii')
        self.assertEqual(int_to_mini_roman(18), 'xviii')
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(20), 'xx')
        self.assertEqual(int_to_mini_roman(21), 'xxi')
        self.assertEqual(int_to_mini_roman(22), 'xxii')
        self.assertEqual(int_to_mini_roman(23), 'xxiii')
        self.assertEqual(int_to_mini_roman(24), 'xxiv')
        self.assertEqual(int_to_mini_roman(25), 'xxv')
        self.assertEqual(int_to_mini_roman(26), 'xxvi')
        self.assertEqual(int_to_mini_roman(27), 'xxvii')
        self.assertEqual(int_to_mini_roman(28), 'xxviii')
        self.assertEqual(int_to_mini_roman(29), 'xxix')
        self.assertEqual(int_to_mini_roman(30), 'xxx')
        self.assertEqual(int_to_mini_roman(31), 'xxxi')
        self.assertEqual(int_to_mini_roman(32), 'xxxii')
        self.assertEqual(int_to_mini_roman(33), 'xxxiii')
        self.assertEqual(int_to_mini_roman(34), 'xxxiv')
        self.assertEqual(int_to_mini_roman(35), 'xxxv')
        self.assertEqual(int_to_mini_roman(36), 'xxxvi')
        self.assertEqual(int_to_mini_roman(37), 'xxxvii')
        self.assertEqual(int_to_mini_roman(38), 'xxxviii')
        self.assertEqual(int_to_mini_roman(39), 'xxxix')
        self.assertEqual(int_to_mini_roman(40), 'xl')
        self.assertEqual(int_to_mini_roman(41), 'xl')
        self.assertEqual(int_to_