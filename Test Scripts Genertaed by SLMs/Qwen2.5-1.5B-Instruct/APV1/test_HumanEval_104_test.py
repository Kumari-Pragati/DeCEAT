system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_104_code import unique_digits
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    odd_digit_elements = []
    for i in x:
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)


assistant

import unittest

# Function to check if a number has only odd digits
def all_odd_digits(n):
    return all(int(digit) % 2 != 0 for digit in str(n))

# Test cases for the unique_digits function
class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
        self.assertEqual(unique_digits([]), [])
        self.assertEqual(unique_digits([17, 19, 23, 29]), [17, 19, 23, 29])

    def test_all_odd_digits(self):
        # Check numbers with no odd digits
        self.assertFalse(all_odd_digits(2))
        self.assertFalse(all_odd_digits(16))
        self.assertTrue(all_odd_digits(15))
        self.assertTrue(all_odd_digits(17))

    def test_strange_cases(self):
        self.assertEqual(unique_digits([-1, -2, -3]), [-1, -2, -3])  # Negative numbers
        self.assertEqual(unique_digits([0]), [])  # Single zero
        self.assertEqual(unique_digits([100, 200, 300]), [])  # Numbers ending in 0 or 2
        self.assertEqual(unique_digits([101, 103, 105]), [101, 103, 105])  # Mixed numbers

if __name__ == '__main__':
    unittest.main()


This code snippet includes a `unique_digits` function and a set of test cases using the `unittest` framework to ensure its correctness. The test cases cover various scenarios including empty lists, single-element lists, negative numbers, and mixed types of numbers.