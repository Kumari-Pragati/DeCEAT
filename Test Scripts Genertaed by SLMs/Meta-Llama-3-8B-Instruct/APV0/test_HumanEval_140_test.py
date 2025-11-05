user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return new_textassistant

Here is the unittest test script for the `fix_spaces` function:

import unittest
from HumanEval_140_code import fix_spaces

class TestFixSpaces(unittest.TestCase):
    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")

    def test_consecutive_spaces(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(fix_spaces("   Example   4"), "_-Example-4")

    def test_no_consecutive_spaces(self):
        self.assertEqual(fix_spaces("Example 5"), "Example_5")

    def test_edge_cases(self):
        self.assertEqual(fix_spaces(""), "")
        self.assertEqual(fix_spaces(" "), "_")

if __name__ == '__main__':
    unittest.main()

This script tests the `fix_spaces` function with various inputs, including:

* No spaces
* Single space
* Multiple spaces
* Consecutive spaces
* Multiple consecutive spaces
* No consecutive spaces
* Edge cases (empty string, single space)

Each test case uses the `assertEqual` method to verify that the output of the `fix_spaces` function matches the expected output.