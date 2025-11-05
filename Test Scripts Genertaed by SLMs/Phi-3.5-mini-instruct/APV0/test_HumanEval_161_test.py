Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_161_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_no_letters(self):
        self.assertEqual(solve("1234"), "4321")

    def test_letters_present(self):
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_letters_and_non_letters(self):
        self.assertEqual(solve("aB1#"), "bAb#")
        self.assertEqual(solve("aB1#c"), "bAb#C")
        self.assertEqual(solve("aB1#C"), "bAb#c")

    def test_empty_string(self):
        self.assertEqual(solve(""), "")

    def test_single_character(self):
        self.assertEqual(solve("a"), "A")
        self.assertEqual(solve("1"), "1")

    def test_mixed_case_letters(self):
        self.assertEqual(solve("AbC"), "aBC")
        self.assertEqual(solve("aBc"), "ABc")

    def test_special_characters(self):
        self.assertEqual(solve("!@#$%^&*"), "!@#$%^&*")

    def test_whitespace(self):
        self.assertEqual(solve("   "), "   ")

if __name__ == '__main__':
    unittest.main()