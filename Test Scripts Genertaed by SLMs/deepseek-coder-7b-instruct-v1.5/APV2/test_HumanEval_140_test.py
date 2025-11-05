You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is the unittest test suite for the given function:


import unittest
from HumanEval_140_code import fix_spaces

class TestFixSpaces(unittest.TestCase):

    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces("Example1"), "Example1")

    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces("Example 2"), "_Example_2")
        self.assertEqual(fix_spaces("Example   3"), "_Example-3")
        self.assertEqual(fix_spaces("Example    4"), "_Example--4")

    def test_leading_spaces(self):
        self.assertEqual(fix_spaces("   Example 1"), "---_Example_1")
        self.assertEqual(fix_spaces("   Example    2"), "---_Example--2")

    def test_trailing_spaces(self):
        self.assertEqual(fix_spaces("Example 1   "), "Example_1---")
        self.assertEqual(fix_spaces("Example    3   "), "_Example--3---")

    def test_mixed_spaces(self):
        self.assertEqual(fix_spaces("   Example 1   "), "---_Example_1---")
        self.assertEqual(fix_spaces("   Example    2   "), "---_Example--2---")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios, including no spaces, single spaces, multiple spaces, leading spaces, trailing spaces, and mixed spaces. Each test checks if the output of the `fix_spaces` function matches the expected result.