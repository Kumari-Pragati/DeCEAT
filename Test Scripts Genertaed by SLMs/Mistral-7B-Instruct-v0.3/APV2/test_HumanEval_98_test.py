You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `count_upper` function:


import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):

    def test_count_upper_empty_string(self):
        self.assertEqual(count_upper(''), 0)

    def test_count_upper_only_uppercase(self):
        self.assertEqual(count_upper('ABCDEFG'), 0)

    def test_count_upper_only_lowercase(self):
        self.assertEqual(count_upper('abcdefg'), 0)

    def test_count_upper_mixed_case(self):
        self.assertEqual(count_upper('aBCdEf'), 1)

    def test_count_upper_vowel_at_even_index(self):
        self.assertEqual(count_upper('dBBE'), 1)

    def test_count_upper_multiple_vowels(self):
        self.assertEqual(count_upper('AeIoU'), 3)

    def test_count_upper_special_characters(self):
        self.assertEqual(count_upper('!@#$%^&*()ABCDEFG'), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty string, only uppercase letters, only lowercase letters, mixed case, vowels at even indices, multiple vowels, and special characters.