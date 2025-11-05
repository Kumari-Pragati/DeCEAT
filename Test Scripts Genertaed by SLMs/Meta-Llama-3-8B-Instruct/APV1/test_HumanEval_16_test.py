user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_16_code import count_distinct_characters
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_count_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters(''), 0)
        self.assertEqual(count_distinct_characters('abc'), 3)
        self.assertEqual(count_distinct_characters('aA'), 2)
        self.assertEqual(count_distinct_characters('Hello, World!'), 10)
        self.assertEqual(count_distinct_characters('1234567890'), 10)
        self.assertEqual(count_distinct_characters('abcdefghijklmnopqrstuvwxyz'), 26)
        self.assertEqual(count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)
        self.assertEqual(count_distinct_characters('!@#$%^&*()_+-='), 13)
        self.assertEqual(count_distinct_characters('   '), 1)
        self.assertEqual(count_distinct_characters('   a   '), 2)
        self.assertEqual(count_distinct_characters('   a   b   '), 3)
        self.assertEqual(count_distinct_characters('   a   b   c   '), 3)
        self.assertEqual(count_distinct_characters('   a   b   c   d   '), 4)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   '), 5)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   '), 6)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   '), 7)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   '), 8)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   '), 9)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   '), 10)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   '), 11)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   '), 12)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   '), 13)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   '), 14)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   '), 15)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   '), 16)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   '), 17)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   '), 18)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   '), 19)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   '), 20)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   '), 21)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   '), 22)
        self.assertEqual(count_distinct_characters('   a   b   c   d   e   f   g   h