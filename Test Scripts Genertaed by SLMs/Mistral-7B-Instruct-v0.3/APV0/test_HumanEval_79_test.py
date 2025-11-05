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

 Here is a unittest test script for the `decimal_to_binary` function:


import unittest
from HumanEval_79_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_decimal_to_binary(self):
        test_cases = [
            (1, "db1db"),
            (2, "db10db"),
            (3, "db11db"),
            (4, "db100db"),
            (5, "db101db"),
            (6, "db110db"),
            (7, "db111db"),
            (8, "db1000db"),
            (9, "db1001db"),
            (10, "db1010db"),
            (11, "db1011db"),
            (12, "db1100db"),
            (13, "db1101db"),
            (14, "db1110db"),
            (15, "db1111db"),
            (16, "db10000db"),
            (255, "db1111111db"),
            (256, "db1000000db"),
            (511, "db11111111db"),
            (1023, "db1111111111db"),
            (1024, "db10000000db"),
            (1025, "db10000001db"),
            (16383, "db10001111111111db"),
            (16384, "db10000000000000db"),
            (32767, "db1111111111111111db"),
            (32768, "db1000000000000000db"),
            (65535, "db111111111111111111db"),
            (65536, "db100000000000000000db"),
        ]
        for decimal, expected in test_cases:
            with self.subTest(f"decimal={decimal}"):
                self.assertEqual(decimal_to_binary(decimal), expected)

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for various decimal numbers and checks if the `decimal_to_binary` function correctly converts them to binary format. The test cases cover a range of small, medium, and large decimal numbers to ensure the function works for a variety of inputs.