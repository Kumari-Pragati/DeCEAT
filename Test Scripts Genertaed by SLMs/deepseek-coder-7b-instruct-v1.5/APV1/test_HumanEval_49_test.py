You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_49_code import modp

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_49_code import modp

class TestModp(unittest.TestCase):
    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case, `test_modp`, which checks the output of the `modp` function against the expected results for a variety of input combinations. The `unittest.TestCase` class provides a number of assertion methods that can be used to check that the actual output matches the expected output.

The `unittest.main()` function call at the end of the script is used to run the test suite. When this script is run, it will execute the tests and report the results.

Please note that the `modp` function is not efficient for large inputs because it uses a loop to calculate the power. It would be more efficient to use the power of two in binary form and the modulo operation distributive property.

Here is an optimized version of the function:


def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    ret = 1
    for bit in bin(n)[2:]:
        ret = (ret * ret) % p
        if bit == '1':
            ret = (ret * 2) % p
    return ret


This version of the function uses bit manipulation to calculate the power of two, which is more efficient for large inputs.