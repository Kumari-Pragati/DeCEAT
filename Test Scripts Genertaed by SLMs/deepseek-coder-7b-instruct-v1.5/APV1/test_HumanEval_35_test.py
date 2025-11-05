You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_35_code import max_element

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):
    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
        self.assertEqual(max_element([-1, -2, -3]), -1)
        self.assertEqual(max_element([1]), 1)
        self.assertEqual(max_element([0, 0, 0]), 0)
        self.assertEqual(max_element([]), None)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases, including positive numbers, negative numbers, a single number, zeros, and an empty list. It checks that the function correctly identifies the maximum element in each case.

Note: In Python, if the list is empty, the function should return `None`, as there is no maximum element in an empty list. This is why there is a test case for an empty list.