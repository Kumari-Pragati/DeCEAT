user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_44_code import change_base
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return retassistant

Here is the unittest test script for the `change_base` function:

import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):
    def test_change_base(self):
        # Test cases from the docstring
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')

        # Additional test cases
        self.assertEqual(change_base(10, 2), '1010')
        self.assertEqual(change_base(15, 8), '17')
        self.assertEqual(change_base(1, 10), '1')
        self.assertEqual(change_base(0, 10), '0')

        # Test edge cases
        self.assertEqual(change_base(-1, 10), '1')  # Negative input
        self.assertEqual(change_base(10, 0), 'Invalid base')  # Invalid base

if __name__ == '__main__':
    unittest.main()

This test script covers the test cases mentioned in the docstring, as well as some additional test cases to ensure the function works correctly for different inputs. It also tests edge cases such as negative input and invalid base.