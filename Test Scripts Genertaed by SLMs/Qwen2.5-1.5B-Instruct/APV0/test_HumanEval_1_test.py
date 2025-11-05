system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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

    return result


assistant

import unittest

# Function to test
from HumanEval_1_code import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):
    def test_single_group(self):
        self.assertEqual(separate_paren_groups("( )"), ["()"])

    def test_multiple_groups(self):
        self.assertEqual(
            separate_paren_groups("( ) (( )) (( )( ))"),
            ["()", "(())", "(()())"]
        )

    def test_empty_input(self):
        self.assertEqual(separate_paren_groups(""), [])

    def test_balanced_groups(self):
        self.assertEqual(
            separate_paren_groups("((()))(())"),
            ["((()))", "(())"]
        )

    def test_nested_groups(self):
        self.assertEqual(
            separate_paren_groups("((((()))))"),
            ["((()))"]
        )

    def test_mixed_groups(self):
        self.assertEqual(
            separate_paren_groups("((()))(())(((())()))"),
            ["((()))", "(())", "((())())"]
        )

if __name__ == '__main__':
    unittest.main()


This script defines a `TestSeparateParenGroups` class that inherits from `unittest.TestCase`. It contains several test methods to ensure the `separate_paren_groups` function works as expected under different scenarios. The `assertEqual` method checks if the output of the function matches the expected results.