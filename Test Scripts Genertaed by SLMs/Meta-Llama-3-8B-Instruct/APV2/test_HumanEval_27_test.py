system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_27_code import flip_case
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):

    def test_flip_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        self.assertEqual(flip_case('WORLD'), 'wORLD')
        self.assertEqual(flip_case('Python'), 'pYTHON')
        self.assertEqual(flip_case(''), '')
        self.assertEqual(flip_case('123'), '123')
        self.assertEqual(flip_case('abcABC'), 'abcABC')

    def test_flip_case_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_flip_case_numbers(self):
        self.assertEqual(flip_case('123'), '123')

    def test_flip_case_punctuation(self):
        self.assertEqual(flip_case('Hello, World!'), 'hELLO, wORLD!')

    def test_flip_case_spaces(self):
        self.assertEqual(flip_case('Hello World'), 'hELLO wORLD')

if __name__ == '__main__':
    unittest.main()