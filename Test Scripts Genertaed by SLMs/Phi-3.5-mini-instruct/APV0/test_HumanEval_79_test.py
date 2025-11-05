Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_79_code import decimal_to_binary
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
        decimal_to_binary(15)   # returns "db1111db"
        decimal_to_binary(32)   # returns "db100000db"
    """

    return "db" + bin(decimal)[2:] + "db"

 import unittest
from HumanEval_79_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary_with_known_values(self):
        # Test with known values
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")
        self.assertEqual(decimal_to_binary(0), "db0db")
        self.assertEqual(decimal_to_binary(1), "db1db")
        self.assertEqual(decimal_to_binary(255), "db11111111db")
        self.assertEqual(decimal_to_binary(256), "db10000000db")

    def test_decimal_to_binary_with_edge_cases(self):
        # Test with edge cases
        self.assertEqual(decimal_to_binary(-1), "db111111111db")  # Negative numbers are not handled
        self.assertEqual(decimal_to_binary(2**31), "db1000000000000000000000000000000db")  # Test with large numbers
        self.assertEqual(decimal_to_binary(2**32), "db10000000000000000000000000000000db")  # Test with even larger numbers

    def test_decimal_to_binary_with_invalid_input(self):
        # Test with invalid input (non-integer)
        with self.assertRaises(TypeError):
            decimal_to_binary("not_an_integer")

if __name__ == '__main__':
    unittest.main()