system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return res.lower()


assistant

import unittest

# Provided code to be tested
from HumanEval_156_code import int_to_mini_roman


class TestIntToMiniRoman(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    def test_edge_cases(self):
        # Edge cases where the input is out of range or invalid
        self.assertIsNone(int_to_mini_roman(-1))
        self.assertIsNone(int_to_mini_roman(1001))

    def test_random_numbers(self):
        # Randomly generated numbers within the valid range
        random_numbers = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000]
        for number in random_numbers:
            result = int_to_mini_roman(number)
            expected_result = f"{number}i"
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


This script includes tests for various scenarios including edge cases (out-of-range inputs), random numbers within the valid range, and specific examples provided in the docstring. It uses `assertEqual` for basic equality checks and `assertIsNone` for checking if an exception occurs when handling invalid inputs. The `unittest.main()` call at the end makes the script executable when run directly.