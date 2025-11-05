system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_85_code import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10]), 20)
        self.assertEqual(add([-2, -4, -6, -8, -10]), -20)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestAdd` class within the `unittest` module, which inherits from `TestCase`. The `test_add` method contains assertions to check the correctness of the `add` function using predefined data points. If any assertion fails, it will raise an error indicating which test failed and what value was expected versus what was actually returned by the function.