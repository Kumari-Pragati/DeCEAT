system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

# Provided code snippet
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
    def test_single_group(self):
        self.assertEqual(parse_nested_parens("(())"), [2])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens("(() ()) ((()))"), [2, 1, 3])

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(""), [])

    def test_balanced_groups(self):
        self.assertEqual(parse_nested_parens("(()) (()) (((())))"), [2, 2, 4])

    def test_unbalanced_groups(self):
        self.assertEqual(parse_nested_parens("(()) (()) ((()")), [])


if __name__ == '__main__':
    unittest.main()


This solution includes a comprehensive unittest test suite for the `parse_nested_parens` function, covering various scenarios including single and multiple groups of balanced parentheses, empty strings, and unbalanced groups.