You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_161_code import solve
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def solve(s):
    """
    You are given a string s.
    - If s[i] is a letter, reverse its case (lower <-> upper).
    - Otherwise, keep it as it is.
    - If the string contains no letters, reverse the string entirely.

    Examples:
        solve("1234") -> "4321"
        solve("ab")   -> "AB"
        solve("#a@C") -> "#A@c"
    """
    flg = 0
    new_str = []

    for i in s:
        if i.isalpha():
            new_str.append(i.swapcase())
            flg = 1
        else:
            new_str.append(i)

    result = "".join(new_str)
    if flg == 0:
        return result[::-1]
    return result


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_161_code import solve

class TestSolve(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(solve("1234"), "4321")

    def test_letters(self):
        self.assertEqual(solve("ab"), "AB")

    def test_special_chars(self):
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_no_letters(self):
        self.assertEqual(solve("123"), "321")

    def test_mixed_chars(self):
        self.assertEqual(solve("aB1#"), "bA1#")

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios:

- When the input string contains only numbers, the function should reverse the string.
- When the input string contains only letters, the function should reverse the case of the letters.
- When the input string contains a mix of letters and special characters, the function should reverse the case of the letters and keep the special characters as they are.
- When the input string contains no letters, the function should reverse the string.
- When the input string contains a mix of letters and numbers, the function should reverse the case of the letters and keep the numbers as they are.

Please note that the function `solve` should be defined in the file `HumanEval_161_code.py`.