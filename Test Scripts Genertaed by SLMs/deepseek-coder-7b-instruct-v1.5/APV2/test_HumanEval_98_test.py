You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return count


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):

    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)
        self.assertEqual(count_upper('A'), 1)
        self.assertEqual(count_upper('b'), 0)
        self.assertEqual(count_upper(''), 0)
        self.assertEqual(count_upper('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 5)
        self.assertEqual(count_upper('abcdefghijklmnopqrstuvwxyz'), 0)
        self.assertEqual(count_upper('AEIOUaeiou'), 5)
        self.assertEqual(count_upper('bBbBbBbB'), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios including strings with uppercase vowels at even indices, strings with uppercase vowels at odd indices, strings with no uppercase vowels, and empty strings.