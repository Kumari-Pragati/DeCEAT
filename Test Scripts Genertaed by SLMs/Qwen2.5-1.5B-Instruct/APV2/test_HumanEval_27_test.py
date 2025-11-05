system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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
    return string.swapcase()


assistant

import unittest

# Provided function
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):
    
    def test_flip_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO', "Test case 1 failed")
        self.assertEqual(flip_case('world'), 'wORLD', "Test case 2 failed")
        self.assertEqual(flip_case('Python'), 'pYTHON', "Test case 3 failed")
        self.assertEqual(flip_case('123abcABC!'), '123ABCabc!', "Test case 4 failed")
        self.assertEqual(flip_case(''), '', "Test case 5 failed")

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases that cover various scenarios including empty strings, strings with mixed case letters, and strings with numbers and special characters. It uses `assertEqual` method to check if the flipped case of each input matches the expected output.