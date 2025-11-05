You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is the unittest script for the given Python function:


import unittest
from HumanEval_85_code import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([1, 3, 5, 7]), 0)
        self.assertEqual(add([2, 4, 6, 8]), 0)
        self.assertEqual(add([1, 2, 3, 4, 5]), 2)
        self.assertEqual(add([10, 20, 30, 40, 50]), 10)
        self.assertEqual(add([1, 3, 5, 7, 9, 11]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10, 12]), 0)
        self.assertEqual(add([1, 2, 3, 4, 5, 6, 7]), 2)
        self.assertEqual(add([10, 20, 30, 40, 50, 60, 70]), 10)
        self.assertEqual(add([1, 3, 5, 7, 9, 11, 13, 15]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10, 12, 14, 16]), 0)

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestAdd` that inherits from `unittest.TestCase`. It includes a method `test_add` that tests the `add` function with a variety of different inputs. Each `self.assertEqual` call checks that the output of the `add` function matches the expected output for a given input.

The script ends with `unittest.main()`, which runs the tests when the script is run directly.

Please note that you need to have the function `add` in the file `HumanEval_85_code.py` for this script to work. If the function is in a different file, you need to import that file instead.