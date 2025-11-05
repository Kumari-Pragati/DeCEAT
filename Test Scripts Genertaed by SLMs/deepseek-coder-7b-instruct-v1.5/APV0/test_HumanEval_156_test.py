You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return res.lower()


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_156_code import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            int_to_mini_roman(0)
        with self.assertRaises(ValueError):
            int_to_mini_roman(1001)
        with self.assertRaises(ValueError):
            int_to_mini_roman(-1)

if __name__ == '__main__':
    unittest.main()


This script includes two test methods:

- `test_valid_input` tests the function with valid inputs from the examples provided in the function's docstring.
- `test_invalid_input` tests the function with invalid inputs that are outside the specified range (1 <= num <= 1000). It uses the `assertRaises` method to ensure that a `ValueError` is raised when an invalid input is provided.

Please note that the function `int_to_mini_roman` should be defined in a file named `HumanEval_156_code.py` for this script to work correctly.