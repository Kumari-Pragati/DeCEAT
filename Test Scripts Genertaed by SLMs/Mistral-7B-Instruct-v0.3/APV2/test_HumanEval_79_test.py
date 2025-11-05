You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `decimal_to_binary` function:


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
            (32, "db100000db"),
            (1024, "db1000000000db"),
            (1025, "db1000000001db"),
            (1026, "db1000000010db"),
            (1027, "db1000000011db"),
            (1028, "db1000000100db"),
            (1029, "db1000000101db"),
            (1030, "db1000000110db"),
            (1031, "db1000000111db"),
            (1032, "db1000001000db"),
            (1033, "db1000001001db"),
            (1034, "db1000001010db"),
            (1035, "db1000001011db"),
            (1036, "db1000001100db"),
            (1037, "db1000001101db"),
            (1038, "db1000001110db"),
            (1039, "db1000001111db"),
            (1040, "db1000010000db"),
            (1041, "db1000010001db"),
            (1042, "db1000010010db"),
            (1043, "db1000010011db"),
            (1044, "db1000010100db"),
            (1045, "db1000010101db"),
            (1046, "db1000010110db"),
            (1047, "db1000010111db"),
            (1048, "db1000011000db"),
            (1049, "db1000011001db"),
            (1050, "db1000011010db"),
            (1051, "db1000011011db"),
            (1052, "db1000011100db"),
            (1053, "db1000011101db"),
            (1054, "db1000011110db"),
            (105