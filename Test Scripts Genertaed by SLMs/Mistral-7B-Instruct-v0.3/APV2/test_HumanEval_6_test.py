You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the `parse_nested_parens` function:


import unittest
from HumanEval_6_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [0])

    def test_single_group(self):
        self.assertEqual(parse_nested_parens('(())'), [2])
        self.assertEqual(parse_nested_parens('()'), [0])
        self.assertEqual(parse_nested_parens('()()'), [0])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens('(()) () ((()))'), [2, 1, 3])
        self.assertEqual(parse_nested_parens('(()) () (()))'), [2, 1, 2])
        self.assertEqual(parse_nested_parens('() () ()'), [0, 0, 0])

    def test_invalid_input(self):
        self.assertRaises(ValueError, parse_nested_parens, '(())(())')
        self.assertRaises(ValueError, parse_nested_parens, '(())()')
        self.assertRaises(ValueError, parse_nested_parens, '()()(')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the edge cases, multiple groups, and invalid inputs. It uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.