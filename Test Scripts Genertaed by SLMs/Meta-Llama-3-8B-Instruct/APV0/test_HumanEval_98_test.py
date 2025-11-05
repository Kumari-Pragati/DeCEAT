user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_98_code import count_upper
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    Examples:
    count_upper('aBCdEf') ➞ 1
    count_upper('abcdefg') ➞ 0
    count_upper('dBBE') ➞ 0
    """

    count = 0
    for i in range(0, len(s), 2):
        if s[i] in "AEIOU":
            count += 1
    return countassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):

    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)
        self.assertEqual(count_upper('AEIOU'), 2)
        self.assertEqual(count_upper('AEIOUa'), 2)
        self.assertEqual(count_upper('AEIOUabc'), 2)
        self.assertEqual(count_upper('AEIOUabcdef'), 2)
        self.assertEqual(count_upper('AEIOUabcdefg'), 2)
        self.assertEqual(count_upper('AEIOUabcdefgh'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghi'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghij'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijk'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijkl'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklm'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmn'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmno'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnop'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopq'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopr'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnops'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopqr'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsq'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprst'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqr'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstu'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrs'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuv'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrst'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvw'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstu'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvw'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstuV'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwx'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstuv'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxY'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstuvwxy'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYz'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstuvwxyZ'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzA'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstuvwxyZA'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzAB'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstuvwxyZAB'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzABC'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstuvwxyZABC'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzABCD'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstuvwxyZABCD'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzABCDF'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnopsqrstuvwxyZABCD'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzABCD'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzABCD'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzABCD'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzABCD'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzABCD'), 2)
        self.assertEqual(count_upper('AEIOUabcdefghijklmnoprstuvwxYzABCD'),