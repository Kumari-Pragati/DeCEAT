You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_23_code import strlen
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

 import unittest
from HumanEval_23_code import strlen

class TestStrlenFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_string_with_characters(self):
        self.assertEqual(strlen('abc'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('a b c'), 3)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen('abc!@#'), 6)

    def test_string_with_numeric_characters(self):
        self.assertEqual(strlen('12345'), 5)

    def test_string_with_mixed_characters(self):
        self.assertEqual(strlen('abc123!@#'), 9)

    def test_string_with_unicode_characters(self):
        self.assertEqual(strlen('áéíóú'), 6)

    def test_string_with_whitespace_and_special_characters(self):
        self.assertEqual(strlen('a b c!@#'), 3)

    def test_string_with_numeric_and_special_characters(self):
        self.assertEqual(strlen('123!@#'), 6)

    def test_string_with_whitespace_and_unicode_characters(self):
        self.assertEqual(strlen('á b c!@#'), 6)

if __name__ == '__main__':
    unittest.main()