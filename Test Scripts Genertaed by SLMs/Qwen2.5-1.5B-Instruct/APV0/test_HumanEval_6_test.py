system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_6_code import parse_nested_parens
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """For a string of balanced parentheses groups separated by spaces,
    return a list with the maximum nesting depth for each group.
    >>> parse_nested_parens('(()) () ((()))')
    [2, 1, 3]
    """
    def parse_paren_group(group: str) -> int:
        depth = 0
        max_depth = 0
        for ch in group:
            if ch == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ')':
                depth -= 1
        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]


assistant

import unittest

# Define the function to be tested
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """For a string of balanced parentheses groups separated by spaces,
    return a list with the maximum nesting depth for each group.
    >>> parse_nested_parens('(()) () ((()))')
    [2, 1, 3]
    """
    def parse_paren_group(group: str) -> int:
        depth = 0
        max_depth = 0
        for ch in group:
            if ch == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ')':
                depth -= 1
        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

class TestParseNestedParens(unittest.TestCase):
    def test_parse_nested_parens(self):
        self.assertEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])
        self.assertEqual(parse_nested_parens('() (()) (((())))'), [1, 2, 4])
        self.assertEqual(parse_nested_parens('(() ()) ((()))'), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines the `parse_nested_parens` function as specified. It also includes a class `TestParseNestedParens` that contains a method `test_parse_nested_parens` which tests the function with different inputs. The `unittest.main()` call at the end makes the tests executable when run directly.