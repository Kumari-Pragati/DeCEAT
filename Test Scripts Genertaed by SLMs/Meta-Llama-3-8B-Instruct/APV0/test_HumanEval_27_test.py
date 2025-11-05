user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the `flip_case` function:

import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        # Test with a simple string
        self.assertEqual(flip_case('Hello'), 'hELLO')

        # Test with a string containing only lowercase characters
        self.assertEqual(flip_case('hello'), 'HELLO')

        # Test with a string containing only uppercase characters
        self.assertEqual(flip_case('HELLO'), 'hello')

        # Test with a string containing a mix of uppercase and lowercase characters
        self.assertEqual(flip_case('HeLlO'), 'hELLO')

        # Test with an empty string
        self.assertEqual(flip_case(''), '')

        # Test with a string containing non-alphabetic characters
        self.assertEqual(flip_case('Hello!'), 'hELLO!')

        # Test with a string containing whitespace
        self.assertEqual(flip_case('Hello World'), 'hELLO wORLD')

if __name__ == '__main__':
    unittest.main()

This test script covers the following scenarios:

1. A simple string with a mix of uppercase and lowercase characters.
2. A string containing only lowercase characters.
3. A string containing only uppercase characters.
4. A string containing a mix of uppercase and lowercase characters.
5. An empty string.
6. A string containing non-alphabetic characters.
7. A string containing whitespace.

Each test case uses the `assertEqual` method to verify that the output of the `flip_case` function matches the expected result.