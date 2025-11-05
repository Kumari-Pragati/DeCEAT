You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return string.swapcase()

 import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):

    def test_flip_case_lowercase_to_uppercase(self):
        self.assertEqual(flip_case('hello'), 'HELLO')

    def test_flip_case_uppercase_to_lowercase(self):
        self.assertEqual(flip_case('WORLD'), 'world')

    def test_flip_case_mixed_case(self):
        self.assertEqual(flip_case('HeLLo'), 'hEllO')

    def test_flip_case_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_flip_case_single_character(self):
        self.assertEqual(flip_case('A'), 'a')
        self.assertEqual(flip_case('1'), '1')

    def test_flip_case_special_characters(self):
        self.assertEqual(flip_case('!@#$%^&*()'), '!@#$%^&*()')

    def test_flip_case_whitespace(self):
        self.assertEqual(flip_case('   '), '   ')

    def test_flip_case_non_alphabetic_characters(self):
        self.assertEqual(flip_case('123!@#$%^&*()'), '123!@#$%^&*()')

if __name__ == '__main__':
    unittest.main()