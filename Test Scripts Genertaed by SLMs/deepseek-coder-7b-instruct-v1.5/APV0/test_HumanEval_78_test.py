You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_78_code import hex_key
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
        For num = "AB" the output should be 1.
        For num = "1077E" the output should be 2.
        For num = "ABED1A33" the output should be 4.
        For num = "123456789ABCDEF0" the output should be 6.
        For num = "2020" the output should be 2.
    """

    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(len(num)):
        if num[i] in primes:
            total += 1
    return total


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_78_code import hex_key

class TestHexKey(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(hex_key(''), 0)

    def test_single_prime(self):
        self.assertEqual(hex_key('2'), 1)

    def test_single_non_prime(self):
        self.assertEqual(hex_key('8'), 0)

    def test_all_primes(self):
        self.assertEqual(hex_key('2357BD'), 6)

    def test_mixed_primes_and_non_primes(self):
        self.assertEqual(hex_key('123456789ABCDEF0'), 6)

    def test_all_non_primes(self):
        self.assertEqual(hex_key('014EAFC682539'), 0)

    def test_single_prime_in_large_number(self):
        self.assertEqual(hex_key('1077E'), 2)

    def test_large_number_with_primes_and_non_primes(self):
        self.assertEqual(hex_key('2020'), 2)

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestHexKey` with several test methods. Each method tests a specific scenario by calling the `hex_key` function with a specific input and then checking if the result matches the expected output.

Note: The script assumes that the `hex_key` function is defined in a file named `HumanEval_78_code.py` and that this file is in the same directory as the unittest script. If the function is defined in a different way or in a different file, the script should be adjusted accordingly.