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
    return string.swapcase()

 Here is a simple unittest test script for the `flip_case` function:


import unittest
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
        self.assertEqual(flip_case('world'), 'wORLD')
        self.assertEqual(flip_case('mIXed CaSe'), 'mIxEd CaSe')
        self.assertEqual(flip_case(''), '')
        self.assertEqual(flip_case('12345'), '12345')
        self.assertEqual(flip_case('Hello, World!'), 'hELLO, wORLD!')

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases for the `flip_case` function, ensuring that it works correctly for different inputs. The test cases cover strings with lowercase, uppercase, mixed case, empty strings, and non-alphabetic strings. The test cases use the `assertEqual` method to verify that the output of the `flip_case` function matches the expected output.