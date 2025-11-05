You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_99_code import closest_integer

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    '''

    from math import floor, ceil

    # Clean up string
    value = value.strip()
    num = float(value)

    # Handle .5 cases — round away from zero
    if abs(num * 10) % 10 == 5:
        return ceil(num) if num > 0 else floor(num)
    else:
        return round(num)


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_numbers(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_edge_cases(self):
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("5.5"), 6)
        self.assertEqual(closest_integer("-5.5"), -5)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            closest_integer("invalid")

if __name__ == '__main__':
    unittest.main()


This suite includes tests for positive numbers, negative numbers, edge cases, and invalid input. It checks that the function returns the correct integer for each of these cases. If the function raises a ValueError when given invalid input, the test will pass. If it does not, the test will fail.