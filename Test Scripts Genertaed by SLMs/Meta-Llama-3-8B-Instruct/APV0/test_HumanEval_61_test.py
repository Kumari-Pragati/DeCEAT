user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_61_code import correct_bracketing
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def correct_bracketing(brackets: str):
    """brackets is a string of "(" and ")".
    Return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0assistant

Here is the unittest test script for the `correct_bracketing` function:

import unittest
from HumanEval_61_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(correct_bracketing(""))

    def test_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_single_closing_bracket(self):
        self.assertFalse(correct_bracketing(")"))

    def test_balanced_brackets(self):
        self.assertTrue(correct_bracketing("()"))
        self.assertTrue(correct_bracketing("(()())"))

    def test_unbalanced_brackets(self):
        self.assertFalse(correct_bracketing(")(("))
        self.assertFalse(correct_bracketing(")(())"))

    def test_multiple_opening_and_closing_brackets(self):
        self.assertTrue(correct_bracketing("((()))"))
        self.assertFalse(correct_bracketing("((())"))

if __name__ == '__main__':
    unittest.main()

This script defines a `TestCorrectBracketing` class with several test methods that cover various scenarios:

1. An empty string
2. A single opening bracket
3. A single closing bracket
4. Balanced brackets (e.g., "()", "(()())")
5. Unbalanced brackets (e.g., ")((", ")(())")
6. Multiple opening and closing brackets (e.g., "((()))", "((())")

Each test method uses the `assert` statement to verify that the `correct_bracketing` function returns the expected result. If the function returns an unexpected result, the test will fail.

To run the tests, simply execute the script. If all tests pass, you should see a message indicating that all tests were successful. If any tests fail, you'll see an error message indicating which test failed and why.