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
    return ret

 Here is a unittest test script for the `change_base` function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 2), '1010')
        self.assertEqual(change_base(15, 3), '212')
        self.assertEqual(change_base(25, 5), '11000')
        self.assertEqual(change_base(12345, 8), '1711')
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(16, 16), '16')
        self.assertEqual(change_base(255, 16), 'ff')

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `change_base` function with various inputs and base numbers. The test case uses the `assertEqual` method to check if the expected output matches the actual output from the function. The test script will run the unittest tests when executed directly.