user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_1_code import separate_paren_groups
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return resultassistant

Here is a unittest test script for the `separate_paren_groups` function:

import unittest
from HumanEval_1_code import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(separate_paren_groups(""), [])

    def test_single_group(self):
        self.assertEqual(separate_paren_groups("( )"), ["( )"])

    def test_multiple_groups(self):
        self.assertEqual(separate_paren_groups("( ) (( )) (( )( ))"), ["()", "(())", "(()())"])

    def test_nested_groups(self):
        self.assertEqual(separate_paren_groups("((()))"), ["((()))"])

    def test_unbalanced_groups(self):
        with self.assertRaises(ValueError):
            separate_paren_groups("(((")

    def test_spaces(self):
        self.assertEqual(separate_paren_groups(" ( ) (( )) (( )( )) "), ["()", "(())", "(()())"])

    def test_multiple_nested_groups(self):
        self.assertEqual(separate_paren_groups("((()))((()))"), ["((()))", "((()))"])

if __name__ == '__main__':
    unittest.main()

This test script covers the following scenarios:

1. An empty input string
2. A single group of parentheses
3. Multiple groups of parentheses
4. Nested groups of parentheses
5. Unbalanced groups of parentheses (should raise a `ValueError`)
6. Input strings with spaces
7. Multiple nested groups of parentheses

Each test method uses the `assertEqual` method to check that the output of the `separate_paren_groups` function matches the expected result. The `assertRaises` method is used to test that the function raises a `ValueError` when given an unbalanced input string.