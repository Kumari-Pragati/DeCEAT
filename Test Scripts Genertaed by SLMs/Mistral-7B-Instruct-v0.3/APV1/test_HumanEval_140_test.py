You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_140_code import fix_spaces

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-" + text[i]
            elif end - start > 0:
                new_text += "_" * (end - start) + text[i]
            else:
                new_text += text[i]
            start, end = i + 1, i + 1
        i += 1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    return new_text

 Here is a comprehensive unittest test suite for the `fix_spaces` function:


import unittest
from HumanEval_140_code import fix_spaces

class TestFixSpaces(unittest.TestCase):

    def test_fix_spaces_single_space(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_fix_spaces_multiple_spaces(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_fix_spaces_leading_space(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")

    def test_fix_spaces_trailing_space(self):
        self.assertEqual(fix_spaces("Example 2 "), "_Example_2")

    def test_fix_spaces_multiple_consecutive_spaces(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_fix_spaces_multiple_consecutive_spaces_at_start(self):
        self.assertEqual(fix_spaces("    Example   3"), "-Example-3")

    def test_fix_spaces_multiple_consecutive_spaces_at_end(self):
        self.assertEqual(fix_spaces("Example   3 "), "_Example-3")

    def test_fix_spaces_multiple_consecutive_spaces_in_middle(self):
        self.assertEqual(fix_spaces("Example   _  3"), "_Example-3")

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including single spaces, multiple spaces, leading spaces, trailing spaces, multiple consecutive spaces at the start, multiple consecutive spaces at the end, and multiple consecutive spaces in the middle.