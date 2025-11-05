You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_85_code import add

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([1, 3, 5, 7]), 0)
        self.assertEqual(add([2, 4, 6, 8]), 0)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7, 8, 9]), 6)
        self.assertEqual(add([10, 20, 30, 40, 50]), 100)
        self.assertEqual(add([1, 3, 5, 7, 9, 11]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10, 12]), 30)
        self.assertEqual(add([1, 3, 5, 7, 9, 11, 13, 15]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10, 12, 14, 16]), 70)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly. It tests the function with a variety of different input lists, including ones with even and odd numbers, and with both even and odd indices.