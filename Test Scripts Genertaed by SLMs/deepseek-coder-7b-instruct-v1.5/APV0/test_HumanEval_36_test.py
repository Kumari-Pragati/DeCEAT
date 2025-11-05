You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_36_code import fizz_buzz
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(50), 0)
        self.assertEqual(fizz_buzz(78), 2)
        self.assertEqual(fizz_buzz(79), 3)
        self.assertEqual(fizz_buzz(100), 2)
        self.assertEqual(fizz_buzz(110), 3)
        self.assertEqual(fizz_buzz(130), 3)
        self.assertEqual(fizz_buzz(111), 3)
        self.assertEqual(fizz_buzz(131), 3)
        self.assertEqual(fizz_buzz(112), 3)
        self.assertEqual(fizz_buzz(132), 3)
        self.assertEqual(fizz_buzz(113), 4)
        self.assertEqual(fizz_buzz(133), 4)
        self.assertEqual(fizz_buzz(114), 4)
        self.assertEqual(fizz_buzz(134), 4)
        self.assertEqual(fizz_buzz(115), 4)
        self.assertEqual(fizz_buzz(135), 4)
        self.assertEqual(fizz_buzz(116), 4)
        self.assertEqual(fizz_buzz(136), 4)
        self.assertEqual(fizz_buzz(117), 4)
        self.assertEqual(fizz_buzz(137), 4)
        self.assertEqual(fizz_buzz(118), 4)
        self.assertEqual(fizz_buzz(138), 4)
        self.assertEqual(fizz_buzz(119), 4)
        self.assertEqual(fizz_buzz(139), 4)
        self.assertEqual(fizz_buzz(120), 5)
        self.assertEqual(fizz_buzz(140), 5)
        self.assertEqual(fizz_buzz(121), 5)
        self.assertEqual(fizz_buzz(141), 5)
        self.assertEqual(fizz_buzz(122), 5)
        self.assertEqual(fizz_buzz(142), 5)
        self.assertEqual(fizz_buzz(123), 5)
        self.assertEqual(fizz_buzz(143), 5)
        self.assertEqual(fizz_buzz(124), 5)
        self.assertEqual(fizz_buzz(144), 5)
        self.assertEqual(fizz_buzz(125), 5)
        self.assertEqual(fizz_buzz(145), 5)
        self.assertEqual(fizz_buzz(126), 5)
        self.assertEqual(fizz_buzz(146), 5)
        self.assertEqual(fizz_buzz(127), 5)
        self.assertEqual(fizz_buzz(147), 5)
        self.assertEqual(fizz_buzz(128), 5)
        self.assertEqual(fizz_buzz(148), 5)
        self.assertEqual(fizz_buzz(129), 5)
        self.assertEqual(fizz_buzz(149), 5)
        self.assertEqual(fizz_buzz(150), 6)

if __name__ == '__main__':
    unittest.main()


This script tests the `fizz_buzz` function with a variety of inputs to ensure that it is working as expected. The test cases are designed to cover a wide range of possible outputs, including edge cases and typical cases.