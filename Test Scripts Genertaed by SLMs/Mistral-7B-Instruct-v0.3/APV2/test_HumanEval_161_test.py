You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the provided `solve` function:


import unittest
from HumanEval_161_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(solve(""), "")

    def test_only_numbers(self):
        self.assertEqual(solve("1234"), "4321")
        self.assertEqual(solve("0123456789"), "9876543210")

    def test_only_letters(self):
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("ABC"), "cBA")
        self.assertEqual(solve("abcdefghijklmnopqrstuvwxyz"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")

    def test_mixed_case_letters(self):
        self.assertEqual(solve("AbCdEfGhIjKlMnOpQrStUvWxYz"), "zYxWvUqRtSnOpMlKjIhGfEdCbAa")
        self.assertEqual(solve("ABCdeFGhIJKlMnOpQrStUvWxYZ"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")

    def test_special_characters(self):
        self.assertEqual(solve("#a@C"), "#A@c")
        self.assertEqual(solve("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), "!@#$%^&*()_+-=[]{}|;:'\",.<>?/")

    def test_empty_string_flg(self):
        self.assertEqual(solve(""), "")

    def test_only_numbers_flg(self):
        self.assertEqual(solve("1234"), "4321")
        self.assertEqual(solve("0123456789"), "9876543210")
        self.assertFalse(solve("1234").count("1234") == solve("4321").count("4321"))

    def test_only_letters_flg(self):
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("ABC"), "cBA")
        self.assertEqual(solve("abcdefghijklmnopqrstuvwxyz"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")
        self.assertFalse(solve("ab").count("ab") == solve("AB").count("AB"))

    def test_mixed_case_letters_flg(self):
        self.assertEqual(solve("AbCdEfGhIjKlMnOpQrStUvWxYz"), "zYxWvUqRtSnOpMlKjIhGfEdCbAa")
        self.assertEqual(solve("ABCdeFGhIJKlMnOpQrStUvWxYZ"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")
        self.assertFalse(solve("AbCdEfGhIjKlMnOpQrStUvWxYz").count("AbCdEfGhIjKlMnOpQrStUvWxYz") == solve("zYxWvUqRtSnOpMlKjIhGfEdCbAa").count("zYxWvUqRtSnOpMlKjIhGfEdCbAa"))

    def test_special_characters_flg(self):
        self.assertEqual(solve("#a@C"), "#A@c")
        self.assertEqual(solve("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), "!@#$%^&*()_+-=[]{}|;:'\